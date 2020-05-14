#!/bin/python3

import math
import os
import random
import re
import sys

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for d in range(2, max(2, int(n ** 0.5)) + 1):
        if n % d == 0:
            return False
    return True


def primeXorHelper(a, i, curr, cache):
    if i > len(a) - 1:
        return 0    

    if not is_prime(a[i]):
        return 0
    
    curr += str(a[i])
    if i < len(a) - 1:
        curr += '-'
    cache[curr] = 1 + max(primeXorHelper(a, i+1, curr, cache), primeXorHelper(a, i+2, curr, cache))
    print(curr)
    return cache[curr]

# Complete the primeXor function below.
def primeXor(a):
    cache = {}
    result = 0
    for i in range(len(a)):
        print(i)
        result += max(result, primeXorHelper(a, i, '', cache))
    return result

print(primeXor([3511, 3671, 4153]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input())

#     for q_itr in range(q):
#         n = int(input())

#         a = list(map(int, input().rstrip().split()))

#         result = primeXor(a)

#         fptr.write(str(result) + '\n')

#     fptr.close()
