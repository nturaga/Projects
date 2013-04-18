function [Time,X] = simpleModelSolver()
t = [1:1:365*25];

% S = 3*10^6;
% I1 = 21;
% I2 = 15;
% P =44;
% T = 15;
% E = S*0.3;

S = 1;
I1 = 0;
I2 = 0;
P = 0;
T = 0;
E = 0;

[Time,X] = ode45(@simpleModel,t,[S E I1 I2 T P]);

plot(Time(1:365:end)/365,X(1:365:end,:));
legend('S','E','I1','I2','T','P');