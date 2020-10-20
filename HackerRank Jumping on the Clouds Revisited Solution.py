# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem


def jumpingOnClouds(c, k):
    n=len(c)

    i=0; jumpsMade = []
    while True:
        if i%n==0 and i!=0:
            break
        jumpsMade.append(c[(i+k)%n])
        i+=k


    energySpent = [3 if jump==1 else 1 for jump in jumpsMade]

    return 100-sum(energySpent)


ans=jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2)
print(ans)
# output
# 92
