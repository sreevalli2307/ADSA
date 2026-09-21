#Task
from typing import List
def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]: 
   directions = [(0,1), (1,0), (0,-1), (-1,0)]
   result = [[rStart, cStart]]
    
   steps = 1   # number of steps in current leg
   d = 0       # direction index
   r, c = rStart, cStart
    
   while len(result) < rows * cols:
        # Each "layer" has two legs of equal step length
        for _ in range(2):
            dr, dc = directions[d]
            for _ in range(steps):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            d = (d + 1) % 4
        steps += 1
    
   return result

   

if __name__ == '__main__':
   rows,cols,rStart,cStart = map(int,input().split())
   print(spiralMatrixIII(rows,cols,rStart,cStart))
