#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 00:07:20 2023

@author: prashantsingh
"""

#https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution1:
    """Implementation 1- ACCEPTED ANSWER - EASY
    ---------------------------------------------------------------------------
    Data Structures-
        n_dict 
            - to store the original index of each element(s).
            - Eg - {2: [0], 3: [1], 4: [2], 5: [3]} 
            
        left_pt - two pointers
        right_pt -
    ---------------------------------------------------------------------------
    Algorithm- 
        1. Save original indexes in a dictionary n_dict.
        2. Sort the array. 
        3. Start searching with two pointer- 
            - if sum(left_pt, right_pt) < target 
                then move left_pt to left (next bigger number)
            else 
                move right_pt to right (next smaller number)

    ---------------------------------------------------------------------------
    Time Complexity - 
        O(n log n) to sort + O(n) to scan the sorted array.
    Space Complexity - 
        O(n) to store indexes.

    ---------------------------------------------------------------------------

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {v: [] for v in nums}
        for k,v in enumerate(nums):
            n_dict[v].append(k)
        
        print(n_dict)
        nums.sort()
        print(nums)
        left_pt = 0
        right_pt = len(nums)-1
        while left_pt < right_pt:
            sum_number = nums[left_pt] + nums[right_pt]
           
            if sum_number == target:
                return [ n_dict[nums[left_pt]][0] , n_dict[nums[right_pt]][-1] ]  

            elif target < sum_number:
                right_pt -=1

            else:
                left_pt += 1
                

Solution1().twoSum(nums=[2,3,4,5,2], target=9)


class Solution2:
    """Implementation 2- ACCEPTED ANSWER
    ---------------------------------------------------------------------------
    Same Algorithm. Somewhat better implementation. 
    Without explicit dictionary.
    Instead convert list to luple of (num, index) and use num to sort the list.
    In this way, you have original index available.
 
    ---------------------------------------------------------------------------

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_index = [(n,index) for index,n in enumerate(nums)] # create tuple of (num,index)
        
        num_index.sort(key=lambda x:x[0]) # sort by first value
        print(nums)
        left_pt = 0
        right_pt = len(nums)-1
        
        while left_pt < right_pt:
            sum_number = num_index[left_pt][0] + num_index[right_pt][0]
           
            if sum_number == target:
                return (num_index[left_pt][1], num_index[right_pt][1])

            elif target < sum_number:
                right_pt -=1

            else:
                left_pt += 1
                

Solution2().twoSum(nums=[2,3,4,5,2], target=9)