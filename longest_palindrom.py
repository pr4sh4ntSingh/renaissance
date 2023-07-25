#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:08:51 2023

@author: prashantsingh
"""
""" 89/141
39/141
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #i,j = self.check_longest_palindrom(s, i=0, j=len(s)-1)
        return self.get_max_palindrom(s)
        #return s[i:j+1] 
        
    def check_longest_palindrom(self,s,i,j):
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
        max_palindrom_index, max_length = (0,0), 0
        # get all substrings
        for i in range(len(s)):
            for j in range(len(s)):
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
