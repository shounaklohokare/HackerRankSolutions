# https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    dosesRequired = 0

    for hurdle in height:
        if hurdle>k:
            dosesRequired = max(hurdle-k, dosesRequired)

    return dosesRequired

ans=hurdleRace(4, [1, 6, 3, 5, 2])
print(ans)

# output
# 2