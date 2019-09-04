
%% ML estimation: 
% our task is to estimate (as good as possible) the "unknown" parameters
% s2, alpha, beta, only using the time series r:

% initial guess:
alpha0 = 0.5;
beta0  = 0.5;
theta0 = [alpha0; beta0];

fun = @(x)-loglf(x, prices);
thetaHat = fmincon(fun,theta0,[],[],[],[],[0;0],[1;1]);

% estimated parameters:
alphaHat = thetaHat(1);
betaHat  = thetaHat(2);

% the corresponding estimated sigma2:
[~,sigma2Hat] = loglf(thetaHat, prices);

% plot the result
figure

subplot(2, 1, 1)
plot(exp(cumsum(prices)))
title('Daily prices','Interpreter','latex')

subplot(2,1,2)
plot(sqrt(250)*sqrt(sigma2))
hold on
plot(sqrt(250)*sqrt(sigma2Hat),'r')
%legend({sprintf('True $(\\alpha,\\beta) = (%3.2f,%3.2f)$',alpha,beta),...
%        sprintf('Estimated $(\\hat{\\alpha},\\hat{\\beta}) = (%3.2f,%3.2f)$',alphaHat,betaHat)},'Interpreter','latex');

%title('Ann. conditional daily std ($\sigma(t)\sqrt{250}$)','Interpreter','latex')