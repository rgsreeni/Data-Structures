# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:30:21 2020

@author: rgsre
"""
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
#represents the coordinate of a point. 
#Check if these points make a straight line in the XY plane.

#Hint: Solve Using Slope

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True
        
        p1 = coordinates[1][1] - coordinates[0][1]             #Y1
        q1 = coordinates[1][0] - coordinates[0][0]             #X1
        
        for i in range(2,len(coordinates)):
            p = (coordinates[i][1] - coordinates[0][1])* q1
            q = (coordinates[i][0] - coordinates[0][0]) * p1
            
            if p != q:
                return False
        
        return True

#Given two strings A and B of lowercase letters
#return True if and only if we can swap two letters in A so that the result... 
#..equals B.

    def buddyStrings(self, A, B):
        """
        :type A: str
        
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False       
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:     
            ind = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    ind.append(i)       
                if counter > 2:
                    return False       
            return A[ind[0]] == B[ind[1]] and A[ind[1]] == B[ind[0]]
    

        
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        
        gi ,si = 0, 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
            si += 1
        return gi
            