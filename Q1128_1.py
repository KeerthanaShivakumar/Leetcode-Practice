# 1128. Number of Equivalent Domino Pairs - Brute force
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]

val = 0
# return val
n = len(dominoes)
for i in range(0, n):
    for j in range(i+1, n):
        ele1 = dominoes[i][0]
        ele2 = dominoes[i][1]
        ele3 = dominoes[j][0]
        ele4 = dominoes[j][1]
        print("ele1: ", ele1, " ele2: ", ele2,
              " ele3: ", ele3, " ele4: ", ele4)
        if((ele1 == ele3 and ele2 == ele4) or (ele1 == ele4 and ele3 == ele2)):
            val = val+1
            print("val inside the loop: ", val)
print("Final answer: ", val)
