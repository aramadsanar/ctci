#!/bin/python3

import math
import os
import random
import re
import sys

def maxSubsetSumHelper(arr, i, curr):
    if i > len(arr) - 1:
        return curr
    
    curr += arr[i]

    return max(maxSubsetSumHelper(arr, i+1, curr), maxSubsetSumHelper(arr, i+2, curr))

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    return maxSubsetSumHelper(arr, 0, 0)

print(maxSubsetSum([3,7,4,6,5]))