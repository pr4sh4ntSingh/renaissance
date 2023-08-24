#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source - https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    """ACCEPTED - OPTIMAL - DYNAMIC PROGRAMMING
    ---------------------------------------------------------------------------
   Algorithm: 
        Now this time houses are in circular order.
        We can break the circle and use house_robber (linear) solution.
        In circle:
            - A - B - C- D - E -
        there are two options- 
          X-  you can leave A and consider B--E as linear
                A || B - C- D - E -
          Y-   or you can leave E and consider A--D as linear houses;
                A - B - C - D -|| E
        Take max of X and Y

    @Prashant Singh
    """

    def house_robber_i(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        number_of_houses = len(nums)
        robbery_sum = [0 for _ in range(number_of_houses)]

        robbery_sum[-1], robbery_sum[-2] = nums[-1],  max(nums[-1], nums[-2])

        for i in range(number_of_houses-3, -1, -1):
            total_amount = nums[i] + max(robbery_sum[i+2:])
            total_amount2 = max(robbery_sum[i+1:])
            robbery_sum[i] = max(total_amount, total_amount2)

        return robbery_sum[0]

    def rob(self, nums: List[int]) -> int:
        ans1 = self.house_robber_i(nums[:-1])
        ans2 = self.house_robber_i(nums[1:])

        return max(ans1, ans2)
