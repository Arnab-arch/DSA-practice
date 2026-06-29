class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        # sliding window algo l and r initial values we will put it in a while loop condition is l<=r then if fruits is not eual at l and r and intially we keep a counter and the maximum lnght of the counter should be 2 so we check if the counter is less than 1 if it is then we append the value if it isnt we do not 
        # [1,2,3,2,2,]  count = 0  l=0 and r=0 arr=[] check count <1 [1]
        #[2] count+=1 [1,2] then count+=1
        maxlen = 0 
        l=0
        n=len(fruits)
        basket={}
        for r in range(n):
            basket[fruits[r]]=basket.get(fruits[r],0)+1
            while len(basket)>2:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                    del basket[fruits[l]]
                l+=1
            maxlen = max(maxlen,r-l+1)
        return maxlen



                    




        