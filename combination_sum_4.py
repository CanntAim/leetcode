class Solution(object):
    numberOfSequences = 0
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print(nums)
        print(target)
        nums.sort()
        if(len(nums) and target >= 0):
            if(target):
                current = nums[0]
                self.combinationSum4(nums[:], target-current)
                nums.pop(0)
                self.combinationSum4(nums[:], target-current)
            else:
                self.numberOfSequences+=1
        return self.numberOfSequences

solution = Solution()
print(solution.combinationSum4([1,2],3))
