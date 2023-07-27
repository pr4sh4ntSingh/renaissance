#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Source  https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    """EASY. ACCEPTED.
    """

    def reverseWords(self, s: str) -> str:
        s_splitted = s.split(" ")
        # since you don't need multiple white spaces, remove all from list.
        s_splitted = list(filter(lambda x: x != '', s_splitted))
        answer = " ".join(x for x in s_splitted[::-1])
        return answer
