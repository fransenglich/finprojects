
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

%% First, we do using Excel
% Our AR(2) data.
exc_ar2 = 0;

% Our numbers from Excel
exc_B0 = 26.5310282;
exc_B1 = 1.323312207;
exc_B2 = -0.3475555766;

% We let the first value be 0.
for i = 2:len
    exc_contr = ar_contribution(prices, i, exc_B0, exc_B1, exc_B2);
    exc_ar2 = [exc_ar2, exc_contr];
end

plot(times, exc_ar2);

%% Now, let's do the regression using Matlab

% Construct our lagged values.
%lag1 = [NaN; prices];
%lag2 = [NaN; NaN; prices];

% Truncate
lag1 = prices(2:end - 2);
lag2 = prices(3:end - 1);
prices = prices(1:end - 3);

len = length(prices);

X = [ones(len, 1) lag1 lag2];

b = regress(prices, X);

B0 = b(1);
B1 = b(2);
B2 = b(3);

matlab_ar2 = 0;

for i = 2:len
    matlab_contr = ar_contribution(prices, i, B0, B1, B2);
    matlab_ar2 = [matlab_ar2, matlab_contr];
end

plot(times(2:end - 2), matlab_ar2);

title("AR(2)");
legend("Wool prices", "OLS in Excel, AR(2)", "OLS in Matlab, AR(2)");
% We get slightly different values for Excel and Matlab, because the data
% sets are slightly different. This is solvable, using different data sets
% for the different approaches.

hold off;