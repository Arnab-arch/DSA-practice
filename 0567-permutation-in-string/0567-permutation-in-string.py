from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        k=len(s1)
        n=len(s2)
        l=0
        if k > n:
            return False
        kmap = Counter(s1)
        window = Counter(s2[:k])

        if kmap == window:
            return True
        for r in range(k,n):
            window[s2[r]]+=1
            window[s2[l]]-=1

            if window[s2[l]]==0:
                del window[s2[l]]
            
            l+=1
            if kmap == window:
                return True
        return False




             



        