'''
kfact
This program computes the k-factor factorization with the lowest spread
Useful for dividing a non-square area into equally sized parcels
Written by Andrew Gilchrist-Scott
'''

from facorize import factorize
from math import *
from Queue import PriorityQueue as PQ
from copy import deepcopy

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

    # let's first do this with a tiny bit of dynamic programming: a tree
    optionsPQ = PQ()
    optionslist = [1]*k
    Root = FactNode(optionsList)

    nodeList = [Root]
    for i in range(len(facts)):
        level = i+1
        factor = facts[i]
        newNodeList = []
        for node in nodeList:
            for j in range(len(node.options)):
                newOptions = node.options[:]
                newOptions[j] *= factor
                node.addChild(newOptions)
            newNodeList += node.children
        nodeList = newNodeList
            
            #TODO
            # for every nod in the list
            # make children for the new fact times every bucket
            # add children to newNodeList


class FactNode(object):

    def __init__(self,options):
        self.options = options
        self.spread = spread(options)
        self.children = []

    def addChild(self, childOptions):
        self.children.append(FactNode(childOptions))

    def isLeaf(self):
        return (len(self.children) == 0)


def spread(lst):
    return max(lst) - min(lst)
    
if __name__ == "__main__":
    for i in range(10,50):
        print(kfact(i,3))
