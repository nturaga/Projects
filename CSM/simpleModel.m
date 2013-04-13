function result = simpleModel(Time,X)

%X(1) = S(t)
%X(2) = E(t)
%X(3) = I1
%X(4) = I2
%X(5) = T
%X(6) = P

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
lamda = 0.3;

result = zeros(6,1);
%S(t)
result(1) = theta* X(5) + epsilon* X(6) - X(1)*lamda;
%E(t)
result(2) = lamda*X(1) - sigma*X(2) - X(2)*pi*delta;
%I1
result(3) = sigma*X(2) - X(3)*pi*delta - gamma*X(3);
%I2
result(4) = gamma*X(3) - alpha*X(4) - X(4)*pi*delta;
%T
result(5) = X(2)*pi*delta + X(3)*pi*delta + X(4)*pi*delta - theta*X(5);
%P
result(6) = alpha*X(4) - epsilon*X(6) - X(6)*pi*delta ;

end
