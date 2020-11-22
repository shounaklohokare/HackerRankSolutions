# https://www.hackerrank.com/challenges/equality-in-a-array/problem?h_r=profile

from collections import  Counter
def equalizeArray(arr):
    c = Counter(arr)
    return len(arr) - max(c.values())