from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n=len(s)
        m=len(p)
        
        if m > n :
            return []
        pmap = Counter(p)
        window = Counter(s[:m])

        l=0
        arr=[]

        if pmap == window :
             arr.append(0)
        for r in range(m,n):
            window[s[r]]+=1
            window[s[l]]-=1

            if window[s[l]]==0:
                del window[s[l]]
            l+=1
            if pmap == window:
                 arr.append(l) 
            
        return arr
        

        

        