%% Simulated data:

% "true" parameters:
s2 = 0.3^2 / 250; % unconditional daily variance
alpha = 0.25;
beta = 0.35;
w = s2 * (1 - alpha - beta);

% simulate a GARCH-time series:
n = 3*250; % 3 years of daily data
e = randn(n,1);
[r,sigma2] = deal(NaN(n,1));
sigma2(1) = s2; % see comments inside log_likelihood
r(1) = sqrt(sigma2(1)) * e(1);
for t = 2:n
    sigma2(t) = w + alpha*r(t-1)^2 + beta*sigma2(t-1);
    r(t) = sqrt(sigma2(t))*e(t);
end

%% ML estimation: 
% our task is to estimate (as good as possible) the "unknown" parameters
% s2, alpha, beta, only using the time series r:

% initial guess:s
alpha0 = 0.5;
beta0  = 0.5;
theta0 = [alpha0; beta0];

fun = @(x)-log_likelihood(x,r);
thetaHat = fmincon(fun,theta0,[],[],[],[],[0;0],[1;1]);

% estimated parameters:
alphaHat = thetaHat(1);
betaHat  = thetaHat(2);

% the corresponding estimated sigma2:
[~,sigma2Hat] = log_likelihood(thetaHat,r);

% plot the result:
figure,
subplot(2,1,1)
plot(exp(cumsum(r)))
title('Daily prices','Interpreter','latex')
subplot(2,1,2)
plot(sqrt(250)*sqrt(sigma2))
hold on
plot(sqrt(250)*sqrt(sigma2Hat),'r')
legend({sprintf('True $(\\alpha,\\beta) = (%3.2f,%3.2f)$',alpha,beta),...
        sprintf('Estimated $(\\hat{\\alpha},\\hat{\\beta}) = (%3.2f,%3.2f)$',alphaHat,betaHat)},'Interpreter','latex');

title('Ann. conditional daily std ($\sigma(t)\sqrt{250}$)','Interpreter','latex')

