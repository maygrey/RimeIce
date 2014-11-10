'''
Challenge 22 Fibonacci Series

Created on 23/09/2014

@author: rpe
'''
import sys
import itertools

def fibonaci():
    """Calculate next Fibonaci"""
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        for line in file:
            Num = int(line)
            #Print out the Numth fibonacci number
            result = list(itertools.islice(fibonaci(), Num, Num + 1))
            print (result.__str__().replace('[','').replace(']',''))
    sys.exit(0)