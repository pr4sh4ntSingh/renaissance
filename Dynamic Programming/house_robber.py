#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source - https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    """ACCEPTED- OPTIMAL - Dynamic Programming
    ---------------------------------------------------------------------------
    Data Structure:
    ---------------
    max_robbed_items : a list where item i tells us the max amount that can be 
    robbed in range i to n.
    Example:
            [26, 16, 16, 15, 8, 12]
                     ^
                  <- i------------||   


    ---------------------------------------------------------------------------
    Algorithm:
    ----------
    nums=[10,1,4,3,8,12], N is Number of houses

    let's start from end. Think what will be answer, 
    a. if there is only one house
    b. if there is only two house. 
        and populate last and second last. 

    Now move forward, at each step you have two choices- 

    1. Leave this house -> 
                        then you can rob neighbors 
                total_amount = max(max_robbed[x+1...N])
    2. Rob this house ->  
                        then you have to leave next neighbor
                total_amount = this house + max(max_robbed[x+2 ... N])

    Why again Max?- 
        because you can choose like this also [1,0,0,1,0,1]


    maximum amount at a given house index x can be calculated via- 



    ---------------------------------------------------------------------------
    @Prashant Singh
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        number_of_houses = len(nums)
        max_robbed_items = [0 for _ in range(number_of_houses)]

        max_robbed_items[-1], max_robbed_items[-2] = nums[-1], nums[-2]

        for i in range(number_of_houses-3, -1, -1):
            # amount in this house nums[i]
            # if rob this house:
            total_amount = nums[i] + max(max_robbed_items[i+2:])
            # if don't rob this house
            total_amount2 = max(max_robbed_items[i+1:])
            max_robbed_items[i] = max(total_amount, total_amount2)

        return max_robbed_items[0]
