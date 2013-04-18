function sensitivity = senstivityAnalysisSimpleModel()

t = [1:1:365*10];

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

sensitivity = [];
for lamda=1:1:10
    disp(['lambda:' num2str(lamda)]);
    [Time,X] = ode45(@(intt,intpos)simpleModelSolver(intt,intpos,lamda), t, [S E I1 I2 I3 T P]);
    sensitivity = [ sensitivity; [lamda, X(end,:)/sum(X(end,:))] ];
end

variables = {'S','E','I1','I2','I3','T','P'};

figure
title('Sensitivity Analysis')
for i=2:1:8
    subplot(4,2,i-1)
    plot(sensitivity(:,1),sensitivity(:,i));
    xlabel('lambda');
    ylabel(variables{i-1});
end
% 
% plot(Time(1:365:end)/365,X(1:365:end,:));
% 
% legend('S','E','I1','I2','I3','T','P');

