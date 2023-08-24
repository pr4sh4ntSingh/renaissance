
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source - https://leetcode.com/problems/house-robber-ii/

class Solution:
    """ACCEPTED- DYNAMIC PROGRAMMING 
    ---------------------------------------------------------------------------
    Algorithm:
            Let's say you have to start from S and Finish at F. 
            There are two intermediate stop P1 and P2.

            S ------> P1 --(there are 12 paths between P1 to F)--->  F
            |                                                        ^
            |                                                        |                                                    |
            ---> P2 --- (there is 15 ways between P2 to F) ----------

            So there will be total 27 ways between S to F. 


    ---------------------------------------------------------------------------
    Data Structure:
        grid [m x n], where each element i,j contains no. of unique path from 
        location [i,j] to Final Location.

        for m=3, n=5 : grid is
                        [[15, 10, 6, 3, 1], 
                        [  5,  4, 3, 2, 1], 
                        [  1,  1, 1, 1, 1]]

    ---------------------------------------------------------------------------
    @Prashant Singh
    """

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1 for _ in range(n)]for _ in range(m)]

        # last value in grid
        grid[-1][-1] = 1

        for i in range(m-1, -1, -1):  # row index
            for j in range(n-1, -1, -1):  # col index
                if i == m-1 and j == n-1:
                    continue

                paths_from_right = grid[i+1][j] if i+1 < m else 0
                paths_from_down = grid[i][j+1] if j+1 < n else 0

                grid[i][j] = paths_from_right + paths_from_down

        return grid[0][0]
