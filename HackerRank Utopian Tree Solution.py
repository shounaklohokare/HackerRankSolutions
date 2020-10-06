# https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    if n==0:
        return 1

    height=0
    for period in range(n+1):
        if period%2!=0:
            height*=2

        else:
            height+=1

    return height

ans=utopianTree(4)
print(ans)
# output
# 7