def formingMagicSquare(s):
    sSpread = [num for ele in s for num in ele] #elements within the nested lists are extracted and kept in a single list.
    
    #magicSquaresComputation = [[a, b, c, d, e, f, g, h, i] for a in range(1, 10) for b in range(1, 10) for c in range(1, 10) for d in range(1, 10) for e in
    #range(1, 10) for f in range(1, 10) for g in range(1, 10) for h in range(1, 10) for i in range(1, 10) if a+b+c==15 and d+e+f==15 and g+h+i==15 and a+d+g==15 and b+e+h==15 and c+f+i==15 and a+e+i==15 and c+e+g==15 and len(set([a, b, c, d, e, f, g, h, i]))==9]
    #Magic Squares are computed by forming all possible lists in which the 9 elements are in range 1 to 9, sum of all rows, columns and
    #diagonals are equal and the lists are unique which is done using List Comprehension.

    #The output of List Comprehension on line 4 and 5 is hardcoded on line 10 and 11 as interpreting the List Comprehension takes much time and is thus not accepted by HackerRank
    magicSquares = [[2, 7, 6, 9, 5, 1, 4, 3, 8], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6], [4, 9, 2, 3, 5, 7, 8, 1, 6],
                    [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 1, 6, 3, 5, 7, 4, 9, 2], [8, 3, 4, 1, 5, 9, 6, 7, 2]]


    costOfChange = []
    for magicSquare in magicSquares:
        costOfChange.append(sum([abs(magicSquare[j]-sSpread[j]) for j in range(9)]))  # the Cost of Change appends the sum of a List Comprehension which computes the
                                                                                      # magnitude by which element needs to change of input list with the list in magic
                                                                                      # magicSquares element

    return min(costOfChange)

formingMagicSquare(input('Enter a list: '))

# Output

# formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]])
# 7

# formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
# 4

#The problem
#https://www.hackerrank.com/challenges/magic-square-forming/problem
