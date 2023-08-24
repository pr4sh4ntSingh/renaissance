#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source https://leetcode.com/problems/jump-game/description/

from typing import List

""" JUMP GAME -I
You are given an integer array nums. 
You are initially positioned at the array's first index, and each element in 
the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    """ACCEPTED - DYNAMIC PROGRAMMING
    ---------------------------------------------------------------------------
    Algorithm:
        start from last and maintain a array can_jump_from, 
        where can_jump_from[i] = True|False.

        can_jump_from(x) = True 
                    only any of [can_jump_from(x).... can_jump_from(x+jump_cap)]
                    is True.

    """

    def canJump(self, nums: List[int]) -> bool:
        can_jump_from = [False for _ in range(len(nums))]

        # from last index one can always reach to last (itself).
        can_jump_from[-1] = True

        for i in range(len(nums)-1, -1, -1):
            jump_capacity = nums[i]
            can_jump_from[i] = any(can_jump_from[i:i+jump_capacity+1])

        return can_jump_from[0]


"""Jump Game II
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
"""
# source - https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    """ACCEPTED - DYNMAIC PROGRAMMING
    """

    def jump(self, nums: List[int]) -> int:
        inf = 999999
        min_jump_from = [inf for _ in range(len(nums))]

        # From last index it will take 0 step to reach at last.
        min_jump_from[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            jump_capacity = nums[i]
            min_jump_from[i] = 1 + min(min_jump_from[i:i+jump_capacity+1])

        return min_jump_from[0]
