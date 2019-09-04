
%% GARCH(1, 1)
subplot(2, 2, [3 4]);
%plot(times, prices);
scatter(times, prices);
hold on;
title("GARCH(1, 1)");

phat = mle(prices);
mean = phat(1);
stddev = phat(2);

model = garch(1, 1);

retval = forecast(model, 20, "Y0", prices, "Constant", NaN);
plot(times, retval);
hold off;


subplot(2, 2, 1);

subplot(2, 2, [3 4]);

%% log returns
subplot(2, 2, 2);
log_returns = diff(log(prices));
plot(times, [log_returns; 0]);
title("log returns");

%% Notes

% See L10S24 on initialization of GARCH



