#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source - https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    """ACCEPTED- OPTIMAL - Dynamic Programming
    ---------------------------------------------------------------------------
    Data Structure:
    ---------------
    nums=[10,1,4,3,8,12], N is Number of houses

    robbery_sum : a list where item i tells us the amount that can be 
    robbed from houses i...N.
    Example:
    robbery_sum=        [26, 16, 16, 15, 12, 12]
                                 ^ 
                              <- i------------||   

    ---------------------------------------------------------------------------
    Algorithm:
    ----------
    Let's start from end. Think what will be answer, 
    a. if there is only one house.
    b. if there is only two house. 
        and populate robbery_sum's  last and second last. 

    Now move forward, at each step you have two choices- 

    1. Leave this house -> 
                        then you can rob neighbor
                total_amount = max(max_robbed[x+1...N])
    2. Rob this house ->  
                        then you have to leave next neighbor
                total_amount = this house + max(max_robbed[x+2 ... N])
    ---------------------------------------------------------------------------
    Time Complexity - O(n^2)
    ---------------------------------------------------------------------------    
    @Prashant Singh
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        number_of_houses = len(nums)
        robbery_sum = [0 for _ in range(number_of_houses)]

        robbery_sum[-1], robbery_sum[-2] = nums[-1],  max(nums[-1], nums[-2])

        for i in range(number_of_houses-3, -1, -1):
            # amount in this house nums[i]
            # if rob this house: then you will have to leave neighor
            total_amount = nums[i] + max(robbery_sum[i+2:])
            # if don't rob this house: then you can add neighbor
            total_amount2 = max(robbery_sum[i+1:])

            # final value will be max of both
            robbery_sum[i] = max(total_amount, total_amount2)

        return robbery_sum[0]
