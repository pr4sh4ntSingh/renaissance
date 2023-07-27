#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:08:51 2023

@author: prashantsingh
"""

class Solution:
    """Implementation 1-  BRUTEFORCE, Not Optimal, TLE 
     ---------------------------------------------------------------------------
     NOTE- this class has two implementations. Checkout commented section in 
     longestPalindrome().
     
     Algorithm:
         1. function  is_palindrom checks if the given string is palindrom
             - Implementation is recursive O(n). (slightly better version could be 
                using for loop.)
         2. Create all substring of the given string - O(n2)
         3. Check all the substrings `get_max_palindrom` for palindrom, return longest.
    ---------------------------------------------------------------------------
    Time Complexity : O(n2)
    Space Complexity : O(n) [if recursion version is used.]
    """
    
    def longestPalindrome(self, s: str) -> str:
        # Check recursively. Passes 39/141 before TLE.
        #i,j = self.check_longest_palindrom(s, i=0, j=len(s)-1)
        #return s[i:j+1] 

        # Passes 89/141 cases before TLE.
        return self.get_max_palindrom(s)

    
    def check_longest_palindrom(self,s,i,j):
        """ i=0, j= len(s)-1 #needs more analysis. #TLE after 39 cases.
            check if s[i:j] is palindrom.
                if not check recusively s[i:j-1] and s[i+1,j] and return max of both.
        """
        #print(f'checking for {s[i:j+1]} ')
        if self.is_palindrome(s, i, j):
            #print(i,j)
            #print(f"palindrom {s[i:j+1]}")
            return (i,j)
        else:
            i1,i2 =self.check_longest_palindrom(s, i+1, j)
            i3,i4 = self.check_longest_palindrom(s, i, j-1)
            print(i1,i2,i3,i4)
            if i2-i1 > i4-i3:
                return (i1,i2)
            else:
                return (i3,i4)
        
    def get_max_palindrom(self,s):
        """start from (0,0) check
        """
        max_palindrom_index, max_length = (0,0), 0
        # get all substrings
        for i in range(len(s)):
            for j in range(j,len(s)):
                if self.is_palindrome(s,i,j):
                    if j-i > max_length:
                        max_length = j-i
                        max_palindrom_index = (i,j)
        
        return s[max_palindrom_index[0]: max_palindrom_index[1]+1]
                        
                    
            

    def is_palindrome(self, s, i, j):
        """Recursively check if string S[i:j] is palindrom or not.
        """
        try:
            if i >= j:
                return True
            elif s[i] == s[j]:
                return self.is_palindrome(s, i+1, j-1)
            else:
                return False
        except IndexError:
            return False


s = "abbcccbbbcaaccbababcbcabca"
Solution().is_palindrome("bb", i=0, j=len(s)-1)
p = Solution().longestPalindrome(s)
print(p)
