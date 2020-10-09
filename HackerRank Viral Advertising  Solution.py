# https://www.hackerrank.com/challenges/strange-advertising/problem


def viralAdvertising(n):
    numOfPeopleAdvertised = 5
    numOfPeopleLiked = numOfPeopleAdvertised//2

    if n==1:
        return numOfPeopleLiked

    totLikes=[2]
    i=0
    while i<n-1:
        i+=1
        numOfPeopleAdvertised=numOfPeopleLiked*3
        numOfPeopleLiked=numOfPeopleAdvertised//2
        totLikes.append(numOfPeopleLiked)


    return sum(totLikes)

ans=viralAdvertising(5)
print(ans)

# output
# 24
