# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i, j, k):

    rangeOfDays = list(range(i, j+1))

    beautifulDays=0
    for day in rangeOfDays:
        reverse = str(day)[::-1]
        if (day-int(reverse))%k==0:
            beautifulDays+=1

    return beautifulDays

ans=beautifulDays(20, 23, 6)
print(ans)

# output
# 2