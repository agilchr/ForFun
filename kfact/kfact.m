% kfact.m
% Program for finding the k-factor factorization of a number with the smallest
% spread. This is useful for dividing a three-dimensional rectangular-prism 
% space into blocks of equal area that are as close to cubes as possible

function facts = kfact(N,K)
    
% obtain a lits of the prime factors of N
    facts = factor(N);
    
    % handles the trivial cases of only enough prime factors to
    % cover k or too few
    if length(facts) == K
        return
    elseif length(facts) < K
        facts = [ones(1,K - length(facts)),facts];
        return
    end
    
    % our ideal value for each factor
    root = N^(1/K);
    
    % if we're foruntate enough to be passed a N such that N^(1/K)
    % is an integer
    if uint64(root) == root
        facts = root*ones(1,K);
        return
    end
    
    % TODO: The difficult part
    
    buckets = ones(1,K);
    
    % Try incrementally adding
    for i = 1:length(facts)
        minSpread = inf;
        for j = 1:K
            new = buckets;
            new(j) = buckets(j)*facts(i);
            if spread(new) < minSpread
                minSpread = spread(new);
                minbuck = j;
            end
        end
        buckets(minbuck) = buckets(minbuck)*facts(i);
    end
    
    facts = buckets;
                
                
function spr = spread(lst)
    spr = max(lst) - min(lst);
        
        
        