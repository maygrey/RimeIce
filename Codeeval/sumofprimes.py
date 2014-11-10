'''
Codeeval challenge 3

Created on 02/06/2014

@author: maygrey
'''
import sys

def search_primes(n):
    """Search all the primes from 2 to n"""
    num = [2]
    i = 3
    while i < n:
        for j in num[:]:
            if i % j == 0:
                i = i + 1
                break
        else:
            num.append(i)
            i = i + 1
    return num
            
def iden_palindrome(num):
    """Identifies all the palindromes in list 'num' """
    tmp = []
    for i in range(len(num)):
        tmp.append(str(num[i]))

    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j] != tmp[i][len(tmp[i])-j-1]:
                break
        else:
            result =tmp[i]
    print(result), 
                   
if __name__ == '__main__':
    """I search all the primes till 1000 and identify the palindromes"""
    primes = search_primes(1000)
    iden_palindrome(primes)
    sys.exit(0)