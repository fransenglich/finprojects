
% Get rid of the figures.
close all;

% Clear the variables.
clear all;

%% Initialize data.
data = readtable("wool.xlsx");

times = data{:, 1};
prices = data{:, 2};


hold on;
plot(times, prices);

len = length(prices);

% Our AR(2) data.
ar2 = 0;

% We let the first value be 0.
for i = 2:len
    contr = ar_contribution(prices, i);
    ar2 = [ar2, contr];
end

plot(times, ar2);
title("AR(2)");
legend("Wool prices", "AR(2)");
hold off;