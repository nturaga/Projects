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
    
    /* callStack to hold frames when functions are called */
    stack callStack = stack_new();
    /* initial program is the "main" function, function 0 (which must exist) */
    struct function_info *main_fn = bc0->function_pool;
    main_fn->num_args = bc0->function_pool->num_args;
    main_fn->num_vars = bc0->function_pool->num_vars;
    main_fn->code_length = bc0->function_pool->code_length;
    main_fn->code = bc0->function_pool->code;
    /* array to hold local variables for function */
    c0_value *V = malloc(sizeof(main_fn->num_vars));
    /* stack for operands for computations */
    stack S = stack_new();
    //    ASSERT(stack_empty(S));
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
	  printf("Pop\n");
	  pop(S);
	  //  printf("%d\n",);
	  pc++;
	  break;
	}
                
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
	      push(S,VAL(v2));
	      push(S,VAL(v1));
	      pc++;
	      break;
	}
	  /* Arithmetic and Logical operations */
          
	case IADD: {
	  printf("In IADD\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  printf("%d\n",x+y);
	  int value = x+y;
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
	case ISUB:{
	  printf("In ISUB\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = y-x;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
	case IMUL:{
	  printf("In IMUL\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x*y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
	case IDIV:{
	  printf("In IDIV\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  if (y ==0){
	    c0_division_error("Zero Division Error");
	  }
	  int value = x/y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IREM:{
	  printf("In IREM\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  if (y ==0){
	    c0_division_error("Zero Division Error");
	  }
	  int value = x%y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IAND:{
	  printf("In IAND\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x&y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}	
                
	case IOR:{
	  printf("In IOR\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x|y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case IXOR:{
	  printf("In IXOR\n");
	  int x = INT(pop(S));
	  int y = INT(pop(S));
	  int value = x^y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
	  
	case ISHL:{
	  printf("In ISHL\n");
	  //Mask "y" by 5 bits, the first value popped off the stack
	  int y = INT(pop(S)) & 0x1F;
	  //The second value popped of the stack
	  int x = INT(pop(S));
	  
	  int value = x<<y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
          
	case ISHR:{
	  printf("In ISHR\n");
	  //Mask "y" by 5 bits, the first value popped off the stack
	  int y = INT(pop(S)) & 0x1F;
	  //The second value popped of the stack
	  int x = INT(pop(S));
	  int value = x>>y;
	  printf("%d\n",value);
	  push(S,VAL(value));
	  pc++;
	  break;
	}
                
             
	  /* Pushing small constants */
	  
	case BIPUSH:{
	  //NEED TO MAKE SURE THE VALUE OF X IS SIGN extended
	  
	  /*Initialize a temp var to store the value from the
	    bytecode in the stack.*/
	  printf("In Bipush\n");
	  int x = (int)((char)P[pc+1]);
	  printf("%d\n",x);
	  push(S,VAL(x));
	  pc = pc + 2;
	  break;
	}
	
	  
                
	  /* Returning from a function */
          
	case RETURN:{
	  printf("In RETURN\n");
	  //  if (!stack_empty(S) && stack_size(S) ==1)
	  // {
	  int return_value = INT(pop(S));
	  free(V);
	  free(S);
	      // }
	  if (stack_empty(callStack))
	    {
	      return return_value;
	    }
	  break;
	}
	  /* frame popped_frame = pop(call_stack); */
	/*   /\*pf is for popped frame*\/ */
	/*   V = popped_frame->V  ; */
	/*   S = popped_frame->S  ; */
	/*   P = popped_frame->P; */
	/*   pc = popped_frame->pc; */
	/*   free(popped_frame); */
	/*   push(return_value,S); */
	/* } */
	  
                
	  /* Operations on local variables */
          
    case VLOAD:{
      
    }
      
    case VSTORE:
      
    case ACONST_NULL:
      
    case ILDC:
      
    case ALDC:
      
      
	  /* Control flow operations */
      
    case NOP:
      
    case IF_CMPEQ:
      
    case IF_CMPNE:
      
    case IF_ICMPLT:
      
    case IF_ICMPGE:
	  
    case IF_ICMPGT:
      
    case IF_ICMPLE:
      
    case GOTO:
      
      
      /* Function call operations: */
      
    case INVOKESTATIC:
      
    case INVOKENATIVE:
      
      
      /* Memory allocation operations: */
      
    case NEW:
      
    case NEWARRAY:
      
    case ARRAYLENGTH:
      
      
      /* Memory access operations: */
      
    case AADDF:
      
    case AADDS:
      
    case IMLOAD:
      
    case IMSTORE:
      
    case AMLOAD:
	  
    case AMSTORE:
      
    case CMLOAD:
      
    case CMSTORE:
      
      
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

