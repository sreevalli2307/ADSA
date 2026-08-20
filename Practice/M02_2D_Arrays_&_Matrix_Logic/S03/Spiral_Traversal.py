'''54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix=list(zip(*matrix)) [::-1] 
        return res       
approach 2
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        top,bottom = 0,rows-1
        left,right = 0,cols-1
        res = []
        while top<= bottom and left<= right:
            #rigth to left
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1
            #top to bottom
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1
            #right to left
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom-=1
            #bottom to top
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left+=1
        return res
        
59. Spiral Matrix II

'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,bottom = 0,n-1
        left,right = 0,n-1
        res = [[0]*n for _ in range(n)]
        num = 1
        while top<= bottom and left<= right:
            #rigth to left
            for col in range(left,right+1):
                res[top][col] = num
                num+=1
            top+=1
            #top to bottom
            for row in range(top,bottom+1):
                res[row][right] = num
                num+=1
            right-=1
            #right to left
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res[bottom][col] = num
                    num+=1
                bottom-=1
            #bottom to top
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res[row][left] = num
                    num+=1
                left+=1
        return res