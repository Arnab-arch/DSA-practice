class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        seen = set(nums)
        missing_element = []

        for i in range(1, n + 1):
            if i not in seen:
                missing_element.append(i)

        return missing_element