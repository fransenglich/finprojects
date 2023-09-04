function [LL,sigma2] = log_likelihood(theta,r)

n = numel(r);

% We follow Sundstrom (2017): https://www.math.kth.se/matstat/seminarier/reports/M-exjobb17/170908b.pdf
%
% Section 2.1 defines the model, with 3 parameters: w, alpha, beta)
% r(t)      = sigma2(t)*e(t)
% sigma2(t) = w + alpha*r(t-1)^2 + beta*sigma2(t-1)
% 
% Section 3.1.1 describes some clever parameter transformations:
% s2   = w / (1 - alpha - beta)

% It is observed that s2 is the unconditional variance, so:
s2 = var(r);
alpha = theta(1);
beta  = theta(2);
w = s2 * (1 - alpha - beta);

% construct the sigma2 time series:
sigma2 = zeros(n,1);
sigma2(1) = s2; % use the unconditional variance as initial value here
for t = 2:n
    sigma2(t) = w + alpha*r(t-1)^2 + beta*sigma2(t-1);
end

% Now that we have sigma2, we can compute the log-likelihood, see Sundstrom's equation (23) on page
% 13. (Omit the first constant term, and the factors 1/2, because those are irrelevant for
% maximization.)
LL = -sum(log(sigma2))-sum(r.^2 ./ sigma2);



