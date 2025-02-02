class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for u in range(len(nums)):
                if nums[i] + nums[u] == target and i != u:
                    return [i, u]
