
% An ML LLF using Gaussian.
%
% args = conditional variance
% data = prices, y
function [retval] = estimate_garch(args, data)
    cond_var = args;
 
    T = length(data);

    % We do the minuses later on.
    part1 = (T/2) * log(2 * pi);

    part2 = 0;
    for t = 1:T
        part2 = part2 + log(cond_var(t)); 
    end
    part2 = part2 / 2;

    part3 = 0;
    for t = 1:T
        y_t = data(t);
        
        c = y_t - ar_contribution(data, t);
        part3 = (part3 + (c)^2)/cond_var(t);
    end
    part3 = part3 / 2;

    % Here's our complete LLF computed.
    retval = - part1 - part2 - part3;
end
