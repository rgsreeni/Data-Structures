# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:38:48 2020

@author: rgsre
"""
#Write a function to return a hint according to the secret number & friends guess,
#use A to indicate the bulls and B to indicate the cows. 

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        bulls = 0
        cows = 0
        bset = set()
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
                bset.add(i)
        cset = set()       
        for j in range(len(guess)):
            for k in range(len(secret)): 
                if j not in bset:
                    if k not in cset and k not in bset and guess[j] == secret[k]:
                        cows += 1
                        cset.add(k)
                        break
        return '{}A{}B'.format(bulls,cows)
    
#Given an array of 2n integers, your task is to group these integers into n pairs 
#of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) 
#for all i from 1 to n as large as possible.
    
    def arrayPairSum(self, nums):
         if len(nums) == 0:
             return 0
         nums.sort()
         sum_min = 0
         for i in range(0,len(nums),2):
             sum_min += nums[i]
         return sum_min
        