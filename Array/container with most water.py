#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    """Bruteforce - ACCEPTED - with TLE (59/63)
    ---------------------------------------------------------------------------
    Algorithm:
    area = min(height[i],height[j]) * (j-i)
    ---------------------------------------------------------------------------
    Time Complexity - O(n2)

    """

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                max_area = area if area > max_area else max_area
        return max_area


class Solution2:
    """Optimal - ACCEPTED 
    ---------------------------------------------------------------------------
    Algorithm:
    Basic idea is still same, but this time use 2 pointers to find max water.
    Start 2 pointers from opposite terminals. Now again- 
    ``area = min(height[l], height[r]) * (r-l)``
    gap:= r-l is always going to decrease in next steps. 
    now whosoever is smaller in height[l], height[r] should not be taken in 
    next step. 


    Example- 
                    l                   r
    if gap is 100, [9 ,a, /......../,b ,3] current area is 100* min(9,3)=300.

    for next step all possible solutins are-
        99* min(9,b)
        99* min(3,a) ---> no matter whatever value of a, this value will always
                          be smaller than previous area 300. 
                          because we are considering min operation over minimum
                          value.


    ---------------------------------------------------------------------------
    Time Complexity - O(n)

    """

    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height)-1, 0

        while l < r:
            # calculate area
            area = min(height[l], height[r]) * (r-l)
            max_area = max(area, max_area)

            # update pointer l,r for next step.
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1

        return max_area
