# https://www.hackerrank.com/challenges/circular-array-rotation/problem


def circularArrayRotation(a, k, queries):
    n=len(a)

    ans=[]
    for q in queries:
        ans.append(a[(n-k+q)%n])

    return ans

ans=circularArrayRotation([1, 2, 3], 2, [0, 1, 2])
print(ans)
# output
# [2, 3, 1]
