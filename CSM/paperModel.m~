function result = paperModel(Time,X)
%X(1) = S(t)
%X(2) = E(t)
%X(3) = I1
%X(4) = I2
%X(5) = I3
%X(6) = T
%X(7) = P

%preference matrix
p = [30,30,30,30,10;5,10,10,5,1;1,2,2,5,0;64,58,58 64 89];
N = X./sum(X);

%parameters given in the paper

sigma = 1/30; %1/days Tranfer of exposed to primary

gamma = 1/45;% transfer rate from primary to secondary syphy

eta = 1/110;% Transfer rate from Secondary syph to further progression of the disese

alpha = 1/30;%Transfer rate from secondary syphlis to become temporarily immune

delta = 1/7; %Transfer rate from all classes to the post-treatment temporary immune class

epsilon = 1/30;%Transfer rate from temporarily
                % immune class to the susceptible
                % class
                
theta = 1/60;%Transfer rate from T to S class

pi = 0.1;%Proportion treated in each class

betaM1 = 0.3;%Transmission probability during
             % primary infection (m: male, f:
             % female)

betaF1 = 0.3;%

betaM2 = 0.45;%

betaF2 = 0.45;%

Vm = 0.05;%Transmission probability during secondary infection

phi = 0.3;%Weight factor of within-group mixing

psi = 0.2; %Weight factor of proportional mixing

v1 = 0.05;
v2 = 0;
v3 = 0;
v4 = 0;
v5 = 0;

lamda = 0.3;

%X(1) = S(t)
%X(2) = E(t)
%X(3) = I1
%X(4) = I2
%X(5) = I3
%X(6) = T
%X(7) = P



result = zeros(7,1);
%S(t)
result(1) = theta* X(6) + epsilon* X(7) + v1 - X(1)*lamda - X(1)*pi*delta;
%E(t)
result(2) = lamda*X(1) + v2 - sigma*X(2) - X(2)*pi*delta;
%I1
result(3) = sigma*X(2) + v3 - X(3)*pi*delta  -gamma*X(3);
%I2
result(4) = gamma*X(3) + v4 - alpha*X(4) - X(4)*pi*delta -  eta*X(4);
%I3
result(5) = eta*X(5) + v5;
%T
result(6) = X(1)*pi*delta + X(2)*pi*delta + X(3)*pi*delta + X(4)*pi*delta - theta*X(6) + X(7)*pi*delta;
%P
result(7) = alpha*X(4) - epsilon*X(7) - X(7)*pi*delta ;

end