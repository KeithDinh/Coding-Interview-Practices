class Solution:
    def spiralOrder(self, matrix):
        result = list()
        sizeRow = len(matrix)
        sizeCol = len(matrix[0])
        num = sizeRow * sizeCol
        
        if sizeRow == 1:
            return matrix[0]
        elif sizeCol == 1:
            return sum(matrix, [])
            
        for d in range(0, sizeRow-1):

            
            for colsTop in range(d, sizeCol-d):
                if num == 0:
                    return result
                else:
                    num -= 1
                result.append(matrix[d][colsTop])
                
            
            for rowsRight in range(d+1, sizeRow-d):
                if num == 0:
                    return result
                else:
                    num -= 1
                result.append(matrix[rowsRight][sizeCol-d-1])
                
            for colsBottom in range(sizeCol-d-2, d-1, -1):
                if num == 0:
                    return result
                else:
                    num -= 1
                result.append(matrix[sizeRow-d-1][colsBottom])
                
            for rowsLeft in range(sizeRow-d-2, d, -1):
                if num == 0:
                    return result
                else:
                    num -= 1
                result.append(matrix[rowsLeft][d])
                
        return result
        