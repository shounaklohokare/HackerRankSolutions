# https://www.hackerrank.com/challenges/acm-icpc-team/problem

def acmTeam(topic):
    ans = []
    for i in range(n):
        for j in range(i, n):
            know = 0
            for (a, b) in zip(topic[i], topic[j]):
                if a=='1' or b=='1':
                    know+=1
            ans.append(know)

    return [max(ans), ans.count(max(ans))]