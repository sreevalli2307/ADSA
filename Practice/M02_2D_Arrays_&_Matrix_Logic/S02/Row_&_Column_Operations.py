'''
1351. Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]<0:
                    count+=(cols-c)
                    break
        return count
approach2:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
       count = 0
       for row in grid:
        for ele in row:
            if ele< 0:
                count+=1
       return count
832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i]=1 if row[i]==0 else 0 
        return image
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] =1 
                else:
                    row[i]=0
        return image

'''