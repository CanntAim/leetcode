class Solution(object):
    maximum = 0
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.decide(0, 0, nums)
        return self.maximum

    def decide(self, current, total, nums):
        if(total > self.maximum):
            self.maximum = total
        if(current > len(nums)-1):
            return 0
        self.decide(current+2,total+nums[current],nums)
        self.decide(current+1,total,nums)

solution = Solution()
print(solution.rob([6000000,20,100,500000,300,3000000000]))
