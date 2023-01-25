class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[] #final result
        for i in range(numRows):
            matrix.append([])
            for j in range(i+1):
                if(j==0 or j==i):
                    matrix[i].append(1)
                else:
                    matrix[i].append(matrix[i-1][j-1]+matrix[i-1][j])
        return matrix