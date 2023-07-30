
# Source https://leetcode.com/problems/spiral-matrix/description/
from typing import List


class Solution:
    """ Medium : Accepted Soulution : 4 pointers. 
    right     left
    ^...   ...^  
    0 1 2 3 4 5   <-- top
    6 7 8 9 9 8      
    7 6 5 4 3 2   <-- bottom 

    Algorithm:
        Use 4 pointers right, left, top, bottom. You will need to move inside
        the boundaries of these 4 pointers. 
        every time you change direction move boundaries also.
        Stop the loop when both left-right and top-bottom collides.

    @CoPilot
    """
    # AI solution

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ls = matrix
        rows = len(ls)
        columns = len(ls[0])
        top = 0
        bottom = rows - 1
        left = 0
        right = columns - 1
        direction = 0
        ans = []
        while top <= bottom and left <= right:
            if direction == 0:  # move right
                for i in range(left, right+1): 
                    ans.append(ls[top][i])  # traverse right along row,
                top += 1
            elif direction == 1:    # move down
                for i in range(top, bottom+1):
                    ans.append(ls[i][right])
                right -= 1
            elif direction == 2:    # move left
                for i in range(right, left-1, -1):
                    ans.append(ls[bottom][i])
                bottom -= 1
            elif direction == 3:    # move up
                for i in range(bottom, top-1, -1):
                    ans.append(ls[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans
