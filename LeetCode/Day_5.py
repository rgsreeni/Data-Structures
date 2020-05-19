# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:59:18 2020

@author: rgsre
"""
#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#Given a balanced string s split it in the maximum amount of balanced strings.
#Return the maximum amount of splitted balanced strings.

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return 0
        
        np = 0
        tmp = s[0]
        count = 1
        for i in s[1:]:
            if tmp == i:
                count += 1
                if count == 0:
                    np += 1
            elif tmp != i:
                count -= 1
                if count == 0:
                    np += 1
                
        return np
    
 #Given a non-empty array of integers, every element appears twice except for one. 
 #Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. implement it without using extra memory?   
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
            
        return a           