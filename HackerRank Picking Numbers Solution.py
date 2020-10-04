# https://www.hackerrank.com/challenges/picking-numbers/problem
from collections import Counter
def pickingNumbers(a):
    arr = Counter(a)
    maxnum=0
    print(arr)
    for i in range(1, 100):
        print(f"for {i} maxnum is {maxnum} and arr[i] is {arr[i]} and arr[i+1] is {arr[i+1]}")
        maxnum = max(maxnum, arr[i+1]+arr[i])
        
    return maxnum

    

pickingNumbers([4, 6, 5, 3, 3, 1])                
