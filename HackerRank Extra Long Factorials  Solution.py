# https://www.hackerrank.com/challenges/extra-long-factorials/problem

from functools import reduce
def extraLongFactorials(n):

    numbers = list(range(1, n+1))

    factorial = reduce((lambda s, x: s*x), numbers)

    print(factorial)

extraLongFactorials(25)
# 15511210043330985984000000
