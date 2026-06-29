class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # we need longest substring means the str whould be continuous what we can do is we add every character in an empty str and check if that chr exists in our str before adding it and iff it does we keep removing elements in the str until we remove the duplicate because we dont need to remove just that emelem we need to remove te duplicate element and the string should be conitnuos there cannot be any break 

        st=""
        maxlen = 0 
        for ch in s:
            while ch in st:
                st = st[1:]  # remove the first element 

            st+=ch
            maxlen = max(maxlen , len(st))
        return maxlen

        # above solution is o(n^2) we can use sets to make it 0(n)

        oset = set()
        l=0
        n=len(s)
        max_len = 0
        for r in range(n):
            while s[r] in s :
                oset.remove(s[l])
                l+=1
            oset.add(s[r])
            max_len = max(max_len , r-l+1)
        return max_len


        
        


            



        