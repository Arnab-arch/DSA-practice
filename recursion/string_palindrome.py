'''125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

approach : 
    first as the question states we only take the characters which are alphabet or nums and then lowercase them 
    then we run a loop from 0 to mid as we know the characters will be checked from the start to the end both will move towards mid 
    as we know the mid element will be same if its palindrome 


'''
def isPalindrome(self,s):
    s="".join(char.lower() for char in s if char.isalnum())
    
    for i in range (0,int(len(s)/2)):
        if s[i]!=s[len(s)-1-i]:
            return False
        return True 
    