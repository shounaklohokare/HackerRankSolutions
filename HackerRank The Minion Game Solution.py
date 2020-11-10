# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    s = len(string)
    vowel = 0    # occurrences of substrings which start with a vowel
    consonant = 0 # occurrences of substring which start with a consonant

    for i in range(s):
        if string[i] in "AEIOU":
            vowel+=(s-i)

        else:
            consonant+=(s-i)

    if vowel<consonant:
        print("Stuart " + str(consonant))

    elif vowel>consonant:
        print("Kevin " + str(vowel))

    else:
        print("Draw")
