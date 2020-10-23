# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    tot_len = len(s)+len(t) ; matched_characters = 0

    for (char_in_s, char_in_t) in zip(s, t):
        if char_in_s==char_in_t:
            matched_characters+=1

    if (2*matched_characters+k>=tot_len and tot_len%2==k%2) or tot_len<k:
        return "Yes"

    else:
        return "No"