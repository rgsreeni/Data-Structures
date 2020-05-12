# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:11:54 2020

@author: rgsre
"""
#We have two special characters. The first character can be represented by one bit 0. 
#The second character can be represented by two bits (10 or 11).

#Now given a string represented by several bits. 
#Return whether the last character must be a one-bit character or not. 
#The given string will always end with a zero.
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
		
		# traverse the list
        while i < len(bits):
			
			#  we need two bits to represent this char, skip to +2th index 
            if bits[i] == 1:
                i += 2
				# last decoded char 2bits long
                flag = False
            else:
                i+=1
				# last decoded char 1 bit long
                flag = True
        return flag
    
#Given two binary strings, return their sum (also a binary string).

#The input strings are both non-empty and contains only characters 1 or 0.
  
    def addBinary(self, a: str, b: str) -> str:
        if len(a) >= len(b):
            smaller = b
            bigger = a
        else:
            smaller = a
            bigger = b
        smaller = smaller.zfill(len(bigger))
        index = len(bigger) -1
        carry = 0
        res = []
        while index >= 0:
            add = int(smaller[index]) + int(bigger[index]) + carry
            res.append(str(add % 2))
            carry = add // 2
            index -= 1
        
        if carry == 1:
            res.append(str(carry))
        res.reverse()
        return "".join(res)