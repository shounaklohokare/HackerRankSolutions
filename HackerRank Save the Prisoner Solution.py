# https://www.hackerrank.com/challenges/save-the-prisoner/problem


def saveThePrisoner(n, m, s):
    res = (s+m-1)%n

    if res==0:
        return n

    return res

ans=saveThePrisoner(3, 7, 3)
print(ans)
# output
# 3