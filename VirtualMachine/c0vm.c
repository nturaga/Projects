#include <assert.h>
#include <limits.h>
#include <stdlib.h>
#include <signal.h>

#include "xalloc.h"
#include "contracts.h"
#include "stacks.h"

#include "bare.h"
#include "c0vm.h"
#include "c0vm_c0ffi.h"
#include<stdio.h>

/* call stack frames */
typedef struct frame * frame;
struct frame {  
    c0_value *V; /* local variables */
    stack S;     /* operand stack */
    ubyte *P;    /* function body */
    int pc;      /* return address */
};


/* functions for handling errors */
void c0_memory_error(char *err) {
    fprintf(stderr, "Memory error: %s\n", err);
    raise(SIGUSR1);
}

void c0_division_error(char *err) {
    fprintf(stderr, "Division error: %s\n", err);
    raise(SIGUSR2);
}


/* TODO: implement execute function */
int execute(struct bc0_file *bc0) {
    
    /* Variables used for bytecode interpreter. You will need to initialize
     these appropriately. */
    
    /* Intialize the VARIABLES*/
    
    /* callStack to hold frames when functions are called */
    stack callStack = stack_new();
    
    /* initial program is the "main" function, function 0 (which must exist) */
    struct function_info *main_fn = bc0->function_pool;
    main_fn->num_args = bc0->function_pool->num_args;
    main_fn->num_vars = bc0->function_pool->num_vars;
    main_fn->code_length = bc0->function_pool->code_length;
    main_fn->code = bc0->function_pool->code;
    /* array to hold local variables for function */
    c0_value *V = malloc(sizeof(c0_value)*main_fn->num_vars);
    
    /* stack for operands for computations */
    stack S = stack_new();
    
    /* array of (unsigned) bytes that make up the program */
    ubyte *P = main_fn->code;
    /* program counter that holds "address" of next bytecode to interpret from
     program P */
    int pc = 0;
    
    while (true) {
        
#ifdef DEBUG
        printf("Executing opcode %x  --- Operand stack size: %d\n",
	       P[pc], stack_size(S));
#endif
        
        switch (P[pc]) {
                
	  /* GENERAL INSTRUCTIONS: Implement the following cases for each of the
	     possible bytecodes.  Read the instructions in the assignment to see
	     how far you should go before you test your code at each stage.  Do
	     not try to write all of the code below at once!  Remember to update
	     the program counter (pc) for each case, depending on the number of
	     bytes needed for each bytecode operation.  See PROG_HINTS.txt for
	     a few more hints.
             
	     IMPORTANT NOTE: For each case, the case should end with a break
	     statement to prevent the execution from continuing on into the
	     next case.  See the POP case for an example.  To introduce new
	     local variables in a case, use curly braces to create a new block.
	     See the DUP case for an example.
             
	     See C_IDIOMS.txt for further information on idioms you may find
                 useful.
	  */
          
	  /* Additional stack operation: */
	case POP: {
	  pop(S);
	  pc++;
	  break;
	}
	  /*Function to duplicate values on the operand stack
                 and then push back 2 values on the OPstack V*/
	case DUP: {
	  c0_value v = pop(S);
	  push(S, VAL(v));
	  push(S, VAL(v));
	  pc++;
	  break;
	}
	  /*Pop both values from the stack and push them
                 back in reverse order into the stack S, increment the
                 counter*/  
	case SWAP: {
	  c0_value v1 = pop(S);
	  c0_value v2 = pop(S);
	  push(S,VAL(v1));
	  push(S,VAL(v2));
	  pc++;
	  break;
            }
	  /* Arithmetic and Logical operations */
          
	case IADD: {
	  /*ADD two values on the operand stack,pop the values and then
	    add and push back 1 result on the stack*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  //RESULT
	  int value = x+y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
	case ISUB:{
	  /*The values on the stack are popped off and we subtract*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = y-x;
	  //Push back the RESULT
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IMUL:{
	  /*The values are popped and multiplied*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x*y;
	  //push back the result of the multiplication
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IDIV:{
	  /* Divide the two popped off values from the stack*/
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  /*Non-intuitive case where the values popped off the stack
	    are INT_MIN and -1, this would cause a division error*/
	  if ((x == INT_MIN) && (y == -1))
	    {
	      c0_division_error("Division Error");
	    }
	  /*WE just cannot divide by 0*/
	  if (y ==0){
	    c0_division_error("Zero Division Error");
	    abort();
                }
	  int value = x/y;
	  //Push the result back on the op stack
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	  /*Edge case to be handled is INT_MIN % -1*/   
	case IREM:{
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  /*The value INT_MIN and -1 cause errors for getting the MOD*/
	  if ((x == INT_MIN) && (y == -1))
                {
		  c0_division_error("Division Error");
                }
	  //Again, we cannot divide by 0
	  if (y ==0){
	    c0_division_error("Zero Division Error");
	    abort();
	  }
	  int value = x%y;
	  // IN all the programs we have to increment the program counter
	  // so that we can move through the byte code.
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IAND:{
	  /* The logic operator allows us to use the AND on two values*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x&y;
	  //Push result on opstack and increment the PC
	  push(S,VAL(value));
	  pc++;
	  break;
	}	
	  
	case IOR:{
	  /* The logic operator allows us to use the OR on two values*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x|y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IXOR:{
	  /* The logic operator allows us to use the XOR on two values*/
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x^y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case ISHL:{
	  /* The logic operator allows us to use the SHIFT LEFT on two values*/
	  //Mask "y" by 5 bits, the first value popped off the stack
	  int y = INT(pop(S)) & 0x1F;
	  //The second value popped of the stack
	  int x = INT(pop(S));
	  //SHIFT LEFT
	  int value = x<<y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case ISHR:{
	  /* The logic operator allows us 
	     to use the SHIFT RIGHT on two values*/
	  //Mask "y" by 5 bits, the first value popped off the stack
	  int y = INT(pop(S)) & 0x1F;
	  //The second value popped of the stack
	  int x = INT(pop(S));
	  //SHIFT RIGHT
	  int value = x>>y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
          
	  /* Pushing small constants */
	  
	case BIPUSH:{
	  //NEED TO MAKE SURE THE VALUE OF X IS SIGN extended
	  
	  /*Initialize a temp var to store the value from the
	    bytecode in the stack.*/
	  int x = (int)((char)P[pc+1]);
	  //Push value on the stack
	  push(S,VAL(x));
	  pc = pc + 2;
	  break;
	}
                
                
                
	  /* Returning from a function */
                
	case RETURN:{
	  /* Pop return value of the op stack*/
	  int return_value = INT(pop(S));
	  //Free the current local variable array and the opStack
	  free(V);
	  free(S);
	  //If callStack is empty, return that value as an int.
	  
	  if (stack_empty(callStack))
	    {
	      return return_value;
	    }
	  //Pop a frame off the callstack.
	  frame popped_frame = pop(callStack);
	  /*pf is for popped frame*/
	  //Restore V, S, P, and pc from the stack frame.
	  V = popped_frame->V;
	  S = popped_frame->S;
	  P = popped_frame->P;
	  pc = popped_frame->pc;
	  //Free the stack frame.
	  free(popped_frame);
	  //Push the return value onto the operand stack.
	  push(S,VAL(return_value));
	  break;
	}
	  
                
	  /* Operations on local variables */
          
	  /*Push the value of a local variable onto the operand
	    stack*/
	case VLOAD:{
	  //Access the value of the by getting the index using
	  //program counter. INDEX  = P[pc+1]. 
	  //Once index is obtained we can access it from the LVA
	  //using the V[INDEX]
	  push(S,V[P[pc+1]]);
	  //Increment the PC by 2
	  pc = pc+2;
	  break;
	}
          
	case VSTORE:{
	  /*pop the value from the top of the stack and store it in a
	    local variable with the vtore instruction*/
	  c0_value x = pop(S);
	  //Same way of getting the index
	  V[P[pc+1]] = x;
	  pc = pc+2;
	  break;
	}
	  /*Push a NULL char*/    
	case ACONST_NULL:{
	  /*The NULL value pushed on the OP stack*/
	  push(S,VAL(NULL));
	  pc++;
	  break;
	}
	  
	  /* ILDC and ALDC take 2 unsigned bytes as operands.
	     The integer pool(int_pool) stores the constants*/    
          
	  
	case ILDC:{
	  /*We are trying to get a interger value
	    which is over a byte from the integer pool*/
	  ubyte val1 = P[pc+1];
	  ubyte val2 = P[pc+2];
	  //Val1 and Val2 give us the index of the 
	  //value in the integer pool
	  push(S,VAL(bc0->int_pool[val1<<8|val2]));
	  pc = pc+3;
	  break;
	}
	  
          
	  /* For strings, the address of the values are put on
	     the operatond stack,S*/    
	case ALDC:{
	  // Index of the string can be obtained by val1 and val2
	  ubyte val1 = P[pc+1];
	  ubyte val2 = P[pc+2];
	  //INDEX is the shift value
	  int shift_value = (int)(val1<<8|val2);
	  //USe the index to get the address of the string from the
	  // string pool as it is in the HEAP
	  push(S,VAL(&bc0->string_pool[shift_value]));
	  pc = pc+3;
	  break;
	}
	  
                
	  /* Control flow operations */
          
	  /*There is no operation performed on the S*/    
	case NOP:{
	  pc++;
	  break;
	}
	  
	case IF_CMPEQ:{
	  //Get the values to incerment the PC
	  ubyte val1 =  P[pc+1];
	  ubyte val2 =  P[pc+2];
	  //POP values of the stack for comparing
	  c0_value y = (pop(S));
	  c0_value x = (pop(S));
	  if (x == y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      //Shift the values to increment the PC
	      pc = (pc + (val1|val2));
	    }
	  //IF x!=y then the PC is incremented normally
	  else{
	    pc= pc+3;
	  }
	  break;
	}
	  
	case IF_CMPNE:{
	  //Get the values to incerment the PC
	  ubyte val1 = P[pc+1];
	  ubyte val2 = P[pc+2];
	  //POP values of the stack for comparing
	  c0_value y = (pop(S));
	  c0_value x = (pop(S));
	  if (x != y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      //Shift the values to increment the PC
	      pc = (pc + (val1|val2));
	    }
	  //IF x==y then the PC is incremented normally
	  else{
	    pc= pc+3;
	  }
	  break;
	}
	  
	  /*THE REST OF THE COMPARE FUNCTIONS are exactly the same
	    but with the comparision changing in each of them*/
            
	  //Compare if LESS THAN    
	case IF_ICMPLT:{
	  ubyte val1 = P[pc+1];
	  ubyte val2 = P[pc+2];
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  if (x < y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      pc = (pc + (val1|val2));
	      
	    }
	  else{
	    pc= pc+3;
	  }
	  break;
	}
	  
	  //Compare if greater than equal to
	case IF_ICMPGE:{
	  
	  ubyte val1 =  P[pc+1];
	  ubyte val2 =  P[pc+2];
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  if (x >= y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      pc = (pc + (val1|val2));
	    }
	  else{
	    pc= pc+3;
	  }
	  break;
	}
	  
	  //Compare if greater than
	case IF_ICMPGT:{
	  
	  ubyte val1 =  P[pc+1];
	  ubyte val2 =  P[pc+2];
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  if (x > y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      pc = (pc + (val1|val2));
	    }
	  else{
	    pc= pc+3;
	  }
	  break;
	}
                
	  //Compare if less than 
	case IF_ICMPLE:{
	  
	  ubyte val1 =  P[pc+1];
	  ubyte val2 = P[pc+2];
	  int y = INT(pop(S));
	  int x = INT(pop(S));
	  if (x <= y)
	    {
	      val1 = (val1<<8);
	      val2 = (val2);
	      pc = (pc + (val1|val2));
	    }
	  else{
	    pc= pc+3;
	  }
	  break;
	}
	  
	  //This implements the jumps in the programs
	case GOTO:{
	  
	  byte val1 = P[pc+1];
	  byte val2 = P[pc+2];
	  pc = (pc+(val1<<8|val2));
	  break;
	}
	  
                
	  /* Function call operations: */
          
	  /*Basic steps:
	    Let fi denote the struct function_info for the called function.
	    1. Build a stack frame containing current code pointer,
	    current pc, current locals, and current operand stack.
	    Push this stack frame onto the call stack.
	    2. Allocate a new locals array of size fi.num_vars.
	    3. Pop fi.num_args values off the stack and put them into
	    the new locals array.
	    4. Create a new, empty operand stack.
	    5. Load the new code into the program array.
	    6. Set the program counter to 0.
	  */
	case INVOKESTATIC:{
	  
	  int val1 =  INT(P[pc+1]);
	  int val2 =  INT(P[pc+2]);
	  int function_index = (val1<<8|val2);
          
	  //New frame with current code pointer,pc,S,V
	  frame new_frame = malloc(sizeof(struct frame));
	  new_frame->P = P;
	  new_frame->pc = pc+3;
	  new_frame->S = S;
	  new_frame->V = V;
          
	  //Push new_frame onto the call stack
	  push(callStack,new_frame);
		
	  //allocate new local variable array
	  struct function_info f = bc0->function_pool[function_index];
	  c0_value* new_LVA = malloc(sizeof(c0_value)*f.num_vars);
          
	  for (int counter = f.num_args -1;counter>=0;counter--)
	    {
	      
	      new_LVA[counter]=pop(S);
	    }
	  //Create a new operand stack
	  stack new_opStack = stack_new();
	  //load new code into the program array
	  P = f.code;
	  //set program counter to 0
	  pc = 0;
	  S = new_opStack;
	  V = new_LVA;
	  break;
	}
	  
          
          
	case INVOKENATIVE:{
	  
	  int val1 =  INT(P[pc+1]);
	  int val2 =  INT(P[pc+2]);
	  //The values are used for calculating the function index
	  int function_index = (val1<<8|val2);
	  //load new code into the program array
	  struct native_info g = (bc0->native_pool[function_index]);
	  //The number of arguments in the function accessed is
                // used to allocate size of the new local var array
	  int g_args = g.num_args;
	  c0_value* new_LVA = malloc(sizeof(c0_value)*g_args);
	  //Put values in the LVA
	  for (int counter =g_args-1;counter>=0;counter--)
                {
		  new_LVA[counter] = pop(S);
                }
	  //push values on the opstack by calling the function
	  // on the array of arguments
	  push(S,
	       native_function_table[g.function_table_index](new_LVA));
	  pc = pc+3;
	  break;
	}                
	  
          
          
                /* Memory allocation operations: */
          
	case NEW:{
	  /*new <s> instruction allocates memory for
	    holding data of size s, and returns the 
	    address of that memory*/
	  int size = P[pc+1];
	  c0_value* new_array =(c0_value*) malloc(size);
	  /*Since "new_array" is an address to the first value on
	    the array*/
	  push(S,new_array);
	  pc+=2;
	  break;
	}
	  
	case NEWARRAY:{
	  /*The newarray <s> instruction allocates memory
	    for an array, each of whose elements has size s.*/
	  int size = P[pc+1];
	  /*Each element in the array has size "size" ;)*/
	  int n =INT (pop(S));
	  c0_array* new_array = malloc(sizeof(struct c0_array) + size*n);
	  new_array->elt_size = size;
	  new_array->count = n;
	  push(S,new_array);
	  pc+=2;
	  break;
	}
	  
	case ARRAYLENGTH:{
	  //Get the array length stored in the c0_array struct
	  c0_array* address = (c0_array*)pop(S);
	  //Length access "count"
	  int array_length = address -> count;
	  push(S,VAL(array_length));
	  pc++;
	  break;
	}
	  
	  /* Memory access operations: */
          
	case AADDF:{
	  //Get the offset from the byte code
	  ubyte offset = P[pc+1];
	  //Pop the address from the stack and add the offset
	  char* stack_address = (char*)(pop(S));
	  //Stack address "a" cannot be NULL
	  push(S,VAL(stack_address+offset));
	  pc+=2;
	  break;
	}
	  
	case AADDS:{
	  //Get values from the stack
	  int array_index = INT(pop(S));
	  struct c0_array* address =  pop(S) ;
	  //Memory errors are to be handled.
	  // we cannot go out of array bounds
	  if (!(array_index>=0 && array_index < address->count))
	    {
	      c0_memory_error("Array index not in bounds");
	      abort();
	    }
	  push(S,(char*)(address)+
	       ((address->elt_size)*array_index)+sizeof(struct c0_array));
	  pc++;
	  break;
	}
	  
	case IMLOAD:{
	  //The function pops an address of the stack 
	  // and loads a addres pointer
	  int* address =(int*) pop(S);
	  //the address can never be NULL
	  if (address == NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	    abort();
	  }
	  push(S,VAL(*address));
	  pc++;
	  break;
	}
	  
	case IMSTORE:{
	  //The function takes the variable and the address from
	  //the stack and then set address equal to the var
	  int x = INT(pop(S));
	  int* a = (int*)(pop(S));
	  //the address can never be NULL
	  if (a==NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	  }
	  ASSERT(a!=NULL);
	  *a = x;
	  pc++;
	  break;
	}
	  
	case AMLOAD:{
	  //Create another variable with same address and 
	  // dereference it
	  c0_value* a = (c0_value*)pop(S);                                
	  //the address can never be NULL
	  if (a==NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	    abort();
	  }
	  ASSERT(a!=NULL);
	  // b is pointing to a
	  c0_value b = *a;
          
	  push(S,b);
	  pc++;
	  break;
	}
	  
          
	case AMSTORE:{
	  //Pop both addresses off the stack
	  c0_value* b = (c0_value*)pop(S);
	  c0_value* a =(c0_value*) pop(S);                                
	  //the address can never be NULL
	  if (a==NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	    abort();
	  }
	  ASSERT(a!=NULL);
	  //set the address of a = b
	  *a = b;
	  pc++;
	  break;
	}
	  
	  //To handle char arrays   
	case CMLOAD:{
	  //Get the char pointer from the stack
	  char* a = (char*)(pop(S));
	  //the address can never be NULL
	  if (a==NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	    abort();
	  }
	  //Set the values x to an int pointer
	  int x = (int)(*a);
	  push(S,VAL(x));
	  pc++;
	  break;
	}
	  
	case CMSTORE:{
	  //Get the values of the char pointer and the int value
	  //from the stack
	  int x = INT(pop(S));
	  char* a = (char*)pop(S);
	  //the address can never be NULL
	  if (a==NULL){
	    c0_memory_error("Dereferencing NULL pointer");
	    abort();
	  }
	  ASSERT(a!=NULL);
	  *a = x & 0x7f;
	  pc++;
	  break;
	}
          
	  
	  fprintf(stderr, "opcode not implemented: 0x%02x\n", P[pc]);
	  abort();
          
	default:
	  fprintf(stderr, "invalid opcode: 0x%02x\n", P[pc]);
	  abort();
        }
        
    }
    
    /* cannot get here from infinite loop */
    assert(false);
}

