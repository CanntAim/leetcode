class Solution(object):
    comp = dict()

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,item in enumerate(nums):
            self.comp[target-item] = index
            if item in self.comp:
                return [self.comp[item],index]
        return []

solution = Solution()
print(solution.twoSum([2,8,11,15],9))
