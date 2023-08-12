#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Source https://leetcode.com/problems/number-of-islands/description/
# Easy, DFS,

"""
To find the number of islands, use DFS search. 
Start from 0,0 visit every node and mark them 'visited.'
For every land travese neighboring using DFS.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    self.visit(grid, i, j)
        return number_of_islands

    def visit(self, grid, x, y):
        try:

            if grid[x][y] == "1":
                grid[x][y] = "6"  # Visited

                self.visit(grid, x+1, y)
                self.visit(grid, x, y+1)
                self.visit(grid, x-1, y)
                self.visit(grid, x, y-1)

        except IndexError:
            pass
