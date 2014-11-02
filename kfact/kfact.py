'''
kfact
This program computes the k-factor factorization with the lowest spread
Useful for dividing a non-square area into equally sized parcels
Written by Andrew Gilchrist-Scott
'''

from factorize import factorize
from math import *
#from Queue import PriorityQueue as PQ
from copy import deepcopy

def kfact(N,K):
    ideal = pow(N,1./K)
    if ideal == floor(ideal):
        # kth root of N is an int, the ideal case
        return [int(ideal)]*K
    
    # obtain the prime factorization
    facts = factorize(N)

    if len(facts) == K:
        # the lucky case
        return facts
    elif len(facts) < K:
        # we've too few factors, so just fill with ones
        while len(facts) < K:
            facts = [1] + facts
        return facts

    # now, the hard part
    # which currently I'm stumped on an ideal not O(len(fact)^k) solution

    # let's first do this with a tiny bit of dynamic programming: a tree
    optionsList = [1]*K
    Root = FactNode(optionsList)

    nodeList = [Root]
    for i in range(len(facts)):
        factor = facts[i]
        newNodeList = []
        for node in nodeList:
            for j in range(len(node.options)):
                newOptions = node.options[:]
                newOptions[j] *= factor
                node.addChild(newOptions)
            newNodeList += node.children
        nodeList = newNodeList
            
    #we have the min spread value somewhere in the leaves of three,
    #now we just have to retrieve it
    (minSpread, bestFactorization) = Root.getMinSpread()

    return bestFactorization
    
class FactNode(object):

    def __init__(self,options):
        self.options = options
        self.spread = self.__spread(options)
        self.children = []

    def addChild(self, childOptions):
        self.children.append(FactNode(childOptions))

    def isLeaf(self):
        return (len(self.children) == 0)

    '''
    Recursive function to get the min spread of the leaves
    '''
    def getMinSpread(self):
        if self.isLeaf():
            return (self.spread,self.options)
        else:
            curMin = float("inf")
            minOptions = []
            min
            for child in self.children:
                (childSpread,childOptions) = child.getMinSpread()
                if childSpread < curMin:
                    curMin = childSpread
                    minOptions = childOptions
            return (curMin, minOptions)


    def __spread(self, lst):
        return max(lst) - min(lst)
    
if __name__ == "__main__":
    for k in range(2,6):
        for i in range(10,71):
            print("The %d lowest spread factors of %d:"%(k,i))
            print(kfact(i,k))
