''' 867
from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Using zip to transpose
        return [list(row) for row in zip(*matrix)]

566
'''