# https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):


    digits = [int(digit) for digit in str(n) if int(digit)!=0]

    answer=0
    for digit in digits:
        if n%digit==0:
            answer+=1

    return answer

ans=findDigits(1012)
print(ans)
# output
# 3