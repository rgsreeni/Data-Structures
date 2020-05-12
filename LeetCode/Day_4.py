# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:07:32 2020

@author: rgsre
"""
#Given an integer, return its base 7 string representation.
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        base = ""
        m = 0
        if num == 0:
            return "0"
        elif num > 0:
            while (7**m) <= num:
                m += 1
            max_m = m - 1
            while max_m >= 0:
                val = num // (7**max_m)
                rem = num % (7**max_m)
                base += str(val)
                num = rem
                max_m -= 1
        
        
            return base
        else:
            num = num * -1
            
            while (7**m) <= num:
                m += 1
            max_m = m - 1
            while max_m >= 0:
                val = num // (7**max_m)
                rem = num % (7**max_m)
                base += str(val)
                num = rem
                max_m -= 1
            
            return "-"+base