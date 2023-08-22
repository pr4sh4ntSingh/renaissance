#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

from typing import List


class Solution:
    """Optimal Soution - ACCEPTED
    ---------------------------------------------------------------------------
    Algorithm:
        sorted array - so use two pointers- at right and left.

        property of sorted array:
            l--->          <---r
        [1, 3 ,4 , 7, 9, 10 , 12, 15, 18, 20]
        sum(l-1,r) <   sum(l,r)   < sum(l,r+1) 
        1+12 = 13  <   3+13 = 15  < 3+15 = 18

        so if your current_sum is smaller -> move left pointer.
        else move right pointer
    ---------------------------------------------------------------------------
    Time Complexity:
        O(n)

    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            sum_ = numbers[r] + numbers[l]
            if sum_ < target:
                l += 1
            elif sum_ > target:
                r -= 1
            else:
                break

        return (l+1, r+1)
