#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    """Bruteforce - ACCEPTED with TLE 308/312
    ---------------------------------------------------------------------------
    Time Complexity - O(n3)

    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        x = [nums[i], nums[j], nums[k]]
                        x.sort()
                        ans.append(tuple(x))
        return set(ans)


class Solution2:
    """ACCETPED | Optimal Solution in Time Complexity
    ---------------------------------------------------------------------------
    Algorithm :
        1. Sort the array -> [-2, -2, 1, 0, 2, 2, 3 ,5]

     [-2, -2, 1, 0, 2, 2, 3 ,5]
      ^    ^-----------------^
      i    j=l                k=r

      now for in array nums[j:k] you need to find target -1*i. 
      You can use 2 pointers to find out that in O(n) in nums[j:k]
      keep updating i, one by one.

    Tricky part is that you don't need duplicates in solution. 
    Maintaining pointer movement to avoid duplicates is possible byt tricky.
    That's why I used set. But it can be done with out set also.
    ---------------------------------------------------------------------------
    Time Complexity - O(n2)
    Space Complexity - O(n)

    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)):
            target = -1 * nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if target < nums[l]+nums[r]:
                    r -= 1
                elif target > nums[l]+nums[r]:
                    l += 1
                else:
                    ans.append(tuple((nums[i], nums[l], nums[r])))
                    # search further
                    r -= 1
                    l += 1

        return set(ans)


nums = [-2, 0, 1, 1, 2]

print(Solution2().threeSum(nums))
