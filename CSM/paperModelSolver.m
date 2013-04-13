function [Time,X] = paperModelSolver()
t = [1:1:365*25];

% S = 3*10^6;
% I1 = 21;
% I2 = 15;
% I3 = 8;
% P =44;
% T = 15;
% E = S*0.3;

S = 1;
I1 = 0;
I2 = 0;
I3 = 0;
P = 0;
T = 0;
E = 0;

[Time,X] = ode45(@WithinGroupMixing,t,[S E I1 I2 I3 T P]);

plot(Time(1:365:end)/365,X(1:365:end,:));
legend('S','E','I1','I2','I3','T','P');