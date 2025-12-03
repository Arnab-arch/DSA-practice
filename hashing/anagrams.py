'''49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

approach : we have to check if each element of the str is same so for that we can use soting if we use sorting is the characters are same they would always be same while sorting

'''


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        map= defaultdict(list)

        for word in strs :
            sort = ''.join(sorted(word))
            map[sort].append(word)
        return list(map.values())

        