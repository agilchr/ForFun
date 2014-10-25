'''
factorize

Program to retrun the prime factorization of a given number, in
ascending order. If the number is prime, that number will be returned in list.

Author: Andrew Gilchrist-Scott
Last updated: October 24, 2014
'''

def factorize(N):
    testProduct = 1
    facts = []

    for i in range(2,N/2 + 1):
        # since the highest factor could only be the number divided in half,
        # we need only look that high

        if (N % i) == 0:
            while testProduct < N:
                if (testProduct*i <= N) and (N%(testProduct*i) == 0):
                    facts.append(i)
                    testProduct *= i
                else:
                    break
        
        if testProduct == N:
            # we've found all the factors
            break
    if facts == []:
        # it's prime
        facts = [N]

    return facts
