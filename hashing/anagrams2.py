'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
'''


class Solution(object):
    def isAnagram(self, s, t):
        s_sort=sorted(s)
        t_sort=sorted(t)

        if s_sort == t_sort:
            return True
        else:
            return False 