

%% GARCH(1, 1)

% We do minus before since we want to maximize with fminunc().
data_carrier = @(x) - estimate_garch(x, prices);

x0 = ones(length(prices), 1);

cond_var = fminunc(data_carrier, x0);