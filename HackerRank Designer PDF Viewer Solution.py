# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):

    letters_ranked = "a b c d e f g h i j k l m n o p q r s t u v q x y  z".split()

    heights = []
    for lett in word:
        pos = letters_ranked.index(lett)
        heights.append(h[pos])

    return max(heights)*len(word)

ans=designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2,5, 5, 5, 5,5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], "zaba")
print(ans)

# Output
# 28