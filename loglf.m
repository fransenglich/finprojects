
% An ML LLF using Gaussian.
function [LL,sigma2] = loglf(theta,r)

    n = numel(r);

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

    % Omit the first constant term, and the factors 1/2, because
    % those are irrelevant for maximization.)
    LL = -sum(log(sigma2))-sum(r.^2 ./ sigma2);
end