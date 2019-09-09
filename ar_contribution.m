% Computes an y_t using values found in argument data, for index index.
%
% Our coefficients from OLS-regression in Excel are 1.323312207 (t - 1) and
% -0.3475555766 (t - 2). Our p-values are accepted with 95% CI. With 3
% variables in the OLS regression one had a poor p-value, so we confine to
% AR(2).
%
% Our equation hence becomes:
%
% y = 26.5310282 + 1.323312207 * y_(t - 1) -0.3475555766 * y_(t - 2)
    
function [retval] = ar_contribution(data, index, B0, B1, B2)

    p1 = 0;
    if index - 1 > 0
        p1 = data(index - 1);
    end
    
    p2 = 0;
    if index - 2 > 0
        p2 = data(index - 2);
    end
    
    retval = B0 + B1 * p1 + B2 * p2;
end