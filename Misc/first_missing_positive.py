#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""
from typing import List


class Solution:
    """ACCEPTED. Not Optimal (in space complexity).
    Time Complexity - O(n)
    Space Complexity - O(n)
    ----------------------------------
    TODO -
    In optimal solution, use nums for the in memory swapping. Use indexes to
    keep track if the item is available or not.
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        lookup_set = set(nums)
        max_num = max(nums)
        for i in range(1, max_num+2):
            if i not in lookup_set:
                return i
        return 1
