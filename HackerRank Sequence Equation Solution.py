# https://www.hackerrank.com/challenges/permutation-equation/problem


def  permutationEquation(p):
    x=list(range(1, len(p)+1))

    indices=[]
    for num in x:
        for i in range(len(p)):
            if p[i]==num:
                indices.append(i+1)

    ans=[]
    for index in indices:
        ans.append(p.index(index)+1)

    return ans

ans=permutationEquation([2, 3, 1])
print(ans)
# Output
# [2, 3, 1]
