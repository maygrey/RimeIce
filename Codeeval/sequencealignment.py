'''
Created on 24/11/2014

Based on Python for Bioinformatics

@author: rpe
'''
import sys
from numpy import zeros
from numpy import array

acgtmat = array([[3, -3, -3, -3], 
                 [-3, 3, -3, -3], 
                 [-3, -3, 3, -3], 
                 [-3, -3, -3, 3]])
pabet = 'ACGT'

def BlosumScore( mat, abet, s1, s2, gap=-8 ):
    sc = 0
    n = min( [len(s1), len(s2)] )
    for i in range( n ):
        print(s1[i])
        print(s1[i-1])
        print(s2[i])
        print(s2[i-1])
        if (s1[i] == '-' or s2[i] == '-') and (s1[i] != s2[i]) and (s1[i-1] == '-' or s2[i-1] == '-' ) and (i > 0):
            print("gap extension")
            sc += -1
        elif s1[i] == '-' or s2[i] == '-' and s1[i] != s2[i]:
            print("gap")
            sc += gap
        elif s1[i] == '.' or s2[i] == '.':
            pass
        else:
            n1 = abet.index( s1[i] )
            n2 = abet.index( s2[i] )
            sc += mat[n1,n2]
    return sc

def BruteForceSlide( mat, abet, seq1, seq2 ):
    # length of strings
    l1, l2 = len(seq1), len(seq2)
    # make new string with leader
    t1 = l2 * '-' + seq1
    t2 = seq2 + l1 * '-'
    lt = len(t1)
    answ = zeros(lt, int)
    for i in range(lt):
        print(i)
        print(t1[i:])
        print(t2)
        answ[i] = BlosumScore(mat, abet, t1[i:], t2)
        print(answ[i])
    return answ


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        for line in file:
            sequence1 = line.split('|')[0].lstrip(' ').split(' ')[0]
            sequence2 = line.split('|')[1].lstrip(' ').split('\n')[0]
            print("h" + sequence1 + "h" + sequence2)
            answ = BruteForceSlide(acgtmat, pabet, sequence1, sequence2)
            print("*********" + str(max(answ)) + "********")
            pass
        
    sys.exit(0)
