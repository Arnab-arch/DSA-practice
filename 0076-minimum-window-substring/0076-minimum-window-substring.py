class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)>len(s):
            return ""
        tmap={}
        for ch in t :
            if ch in tmap:
                tmap[ch]+=1
            else:
                tmap[ch]=1
        missing = len(t)
        l=0
        start=0
        n=len(s)
        min_len = float('inf')
        for r in range(n):
            if s[r] in tmap:
                if tmap[s[r]]>0:
                    missing-=1
                tmap[s[r]]-=1
            while missing==0:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    start = l 
                if s[l] in tmap:
                    tmap[s[l]]+=1
                    if tmap[s[l]]>0:
                        missing+=1
                
                l+=1
        return "" if min_len==float('inf') else s[start:start+min_len]


        

                


        