#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player.sort(reverse=True)
    print(ranked, player)

    l=len(ranked)
    j=0

    result=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        result.append(j+1)

    return result[::-1]

result=climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])
print(result)

# output
# [6, 4, 2, 1]