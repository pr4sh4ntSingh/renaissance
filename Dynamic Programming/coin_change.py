#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/coin-change/
"""
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
 coins = [1,2,5], amount = 11
"""
from typing import List


class Solution:
    """ACCEPTED - OPTIMAL - FA
    ---------------------------------------------------------------------------
    Algorithm: 
        number of coins required for amount is - 
        if 
            coin of exact denomination is available then 1 
        otherwise
             coin(amount) = 1 + min[coin(amount - a), coint(amount -b).....coin(amount-z)]
             where a,b...z are available denominations.


    So we need to populate 1D lookup table. We start from 0 and use above formulae.
    ---------------------------------------------------------------------------
    Data Structure:
        for -> coins = [1,2,5], amount = 11
        lookup_array:                [0, inf, inf ......]
        final lookup_array:          [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        index is amount:            ^[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    ---------------------------------------------------------------------------
    Time Complexity:
        O(n)
    @Prashant Singh
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        
        INF = 999999
        lookup_array = [INF for _ in range(amount+1)]
        lookup_array[0] = 0  # because for amount 0, 0 coins are needed
        coin_set = set(coins)

        for amount in range(len(lookup_array)):
            if amount in coin_set:
                lookup_array[amount] = 1
            else:
                m = [lookup_array[amount-j] for j in coin_set if amount-j > 0]
                # min_ = min(m) if len(m) > 0 else inf
                # lookup_array[amount] = 1 + min_
                lookup_array[amount] = 1 + min(m+[INF])

        ans = lookup_array[-1]
        return ans if ans < INF else -1
