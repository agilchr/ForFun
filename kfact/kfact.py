'''
kfact
This program computes the k-factor factorization with the lowest spread
Useful for dividing a non-square area into equally sized parcels
Written by Andrew Gilchrist-Scott
'''

from facorize import factorize
from math import *
from Queue import PriorityQueue as PQ

def kfact(N,K):
    ideal = pow(N,1./K)
    if ideal == floor(ideal):
        # kth root of N is an int, the ideal case
        return [ideal]*K
    
    # obtain the prime factorization
    facts = factorize(N)

    if len(facts) == K:
        # the lucky case
        return facts
    elif len(facts) < K:
        # we've too few factors, so just fill with ones
        while len(facts) < K:
            facts = [1] + facts

    # now, the hard part
    # which currently I'm stumped on an ideal not O(len(fact)^k) solution

    # let first brute force this
    optionsPQ = PQ()
    optionslist = [[1]*k]

    for factor in facts:
        newOptions = []
        for option in optionsList:
            for i in len(


def spread(lst):
    return max(lst) - min(lst)
    
if __name__ == "__main__":
    for i in range(10,50):
        print(kfact(i,3))
