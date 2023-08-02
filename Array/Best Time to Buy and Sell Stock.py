#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# source https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    """ Optimal Solution, ACCEPTED, 
    ---------------------------------------------------------------------------
    Data Structures:
        running_max_list[i] =: max value that stock will take time [i..n]
        max_profits[i] =: max benefit if bought at time i.

        Example-
        prices = [7,1,5,3,6,4]
        running_max_list = [7, 6, 6, 6, 6, 4]
        max_profits = [0, 5, 1, 3, 0, 0]
    ---------------------------------------------------------------------------
    Algorithm:
    1 - Start with last index and populate running_max_list with max value.
    2 - max_profits is just running_max_list[i] - prices[i]
    3 - Return max of max_profits.
    ---------------------------------------------------------------------------
    Complexity:
    Time - O(n)
    Space- O(n)
    """

    def maxProfit(self, prices: List[int]) -> int:
        m = len(prices)
        running_max_list = [0 for _ in range(m)]
        max_profits = [0 for _ in range(m)]
        running_max = 0
        for i in range(m-1, -1, -1):
            if prices[i] > running_max:
                running_max = prices[i]
            running_max_list[i] = running_max

        for i in range(m):
            max_profits[i] = running_max_list[i] - prices[i]
        return max(max_profits)


# %%


class Solution2:
    """ Not Optimal Solution, ACCEPTED, Bruteforce, 198/212 TLE.
    ---------------------------------------------------------------------------
    ---------------------------------------------------------------------------
    Algorithm:
        start with each day i, find max_profit that you can get if you buy at 
        that day[i].
        keep track of max value.
    ---------------------------------------------------------------------------
    Complexity:
    Time - O(n2)
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):  # buy at day i
            for j in range(i+1, len(prices)):  # sell at day j

                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
