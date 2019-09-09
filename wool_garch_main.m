clear all;
close all;

%% Initialize data.
data = readtable("wool.xlsx");

times = data{:, 1};
prices = data{:, 2};

len = length(prices);
simu_len = 3 * 250;

%% True test data parameters
s2 = 0.3^2 / 250; % unconditional daily variance.
alpha = 0.25;
beta = 0.35;
w = s2 * (1 - alpha - beta);

%% Simulate test data
e = randn(simu_len, 1);
[simulated, simu_sigma2] = deal(NaN(simu_len, 1));
simu_sigma2(1) = s2;
simulated(1) = sqrt(simu_sigma2(1)) * e(1);
for t = 2:simu_len
    simu_sigma2(t) = w + alpha * simulated(t - 1)^2 + beta * simu_sigma2(t - 1);
    simulated(t) = sqrt(simu_sigma2(t)) * e(t);
end

%% ML estimation: 

% initial guess:
simu_alpha0 = 0.5;
simu_beta0 = 0.5;
simu_theta0 = [simu_alpha0; simu_beta0];

simu_fun = @(x)-loglf(x, simulated);
simu_thetaHat = fmincon(simu_fun, simu_theta0, [], [], [], [], [0;0], [1;1]);

% the corresponding estimated sigma2:
[~, simu_sigma2Hat] = loglf(simu_thetaHat, simulated);

% plot the result
figure

%% Basic view of our data to aid intuition
subplot(3, 1, 1)

plot(times, prices);
title("Wool prices, plain time series.");


%% Let's plot our computed and simulated variance
subplot(3, 1, 2)

% The real variance, we computed it.
plot(sqrt(250)*sqrt(simu_sigma2), 'g');

hold on;
plot(sqrt(250)*sqrt(simu_sigma2Hat),'r');
title("GARCH on simulated data.");

plot(simulated);

legend("Real std. dev.", "Std. dev. from GARCH(1, 1)", "Time series");

hold off;

%% Let's now run on the actual wool prices
alpha0 = 0.5;
beta0  = 0.5;
theta0 = [alpha0; beta0];

fun = @(x)-loglf(x, prices);
thetaHat = fmincon(fun, theta0, [], [], [], [], [0;0], [1;1]);

[~, sigma2Hat] = loglf(thetaHat, prices);

subplot(3, 1, 3)

plot(times, sqrt(sigma2Hat));
title("GARCH(1, 1) std. dev. of wool data.");
