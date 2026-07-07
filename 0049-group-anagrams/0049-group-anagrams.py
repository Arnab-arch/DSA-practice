from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # we can use a dict so my logic would be to create an empty dictinary and what is the pattern here if we take the eords that are anagrams what is common in [eat tea ate ] the common thing in this is if we sort these words they will all be same so cant we just check for the words sorted that gives the same value and put in in group 
        # so make the sorted words as key and if another word after sorting produce this key add that then we just return the hashmap 
        groups = defaultdict(list)    #so this makes a hashmap and the default value if it occurs first time returns [] empty list 
        for word in strs:
            key = "".join(sorted(word))  #sorted will return a list of indiviual ch in words so we just join them
            groups[key].append(word) # if the same key appears we just add the word to the values 

        return list(groups.values())
        
