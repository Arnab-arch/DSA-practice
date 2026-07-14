class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for interval in intervals :
            # when the interval is less than new interval we just add it in the array 
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0]>newInterval[1]:
                ans.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
                # we are not appending this in the array because we dont know if we have to add more values or there are more continous overlaps in the array 
        ans.append(newInterval)
        return ans 






        