'''
This is an attempt to make a bounded int class in Python.

Ideal:
* it will act as an int in all circumstances, except:
  - it's value cannot go below MIN
  - it's value cannot go above MAX
* user can control wrapped (mod) vs capped (hold val to max or min if it goes
  above or below). Default is capped.

This class should never be used in place of an int if size or speed is an issue;
it's merely a convenience.

Useful: https://docs.python.org/2/library/operator.html

Author: Andrew Gilchrist-Scott
'''

class BoundedInt(object):

    def __init__(self, inMin = -float("inf"), inMax = float("inf"), boundingStyle = "cap"):
        self.MIN = inMin
        self.MAX = inMax
        self.val = 0
        boundingStyle = boundingStyle.lower()
        if boundingStyle == 'wrap':
            self.capNotWrap = False
        else:
            self.capNotWrap = True

    def __str__(self):
        return str(self.val)

    def set(self,val):
        if val < self.MIN:
            if self.capNotWrap:
                val = self.MIN
            else:
                while not (self.MIN <= val <= self.MAX):
                    val += (self.MAX - self.MIN)
        elif val > self.MAX:
            if self.capNotWrap:
                val = self.MAX
            else:
                while not (self.MIN <= val <= self.MAX):
                    val -= (self.MAX - self.MIN)
        self.val = val

    def __add__(self,b):
        if type(b) == type(self):
            return self.val + b.val
        else:
            return self.val + b
