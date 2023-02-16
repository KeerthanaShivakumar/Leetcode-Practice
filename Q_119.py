# 119. Pascal's Triangle II
n = int(input())
#display the last row of pascal triangle given n

matrix=[] #final result
for i in range(n):
    matrix.append([])
    for j in range(i+1):
        if(j==0 or j==i):
            matrix[i].append(1)
        else:
            matrix[i].append(matrix[i-1][j-1]+matrix[i-1][j])
print(matrix[-1])