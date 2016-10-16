class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stopped_increasing = False

        for i in range(len(nums)):
            if(i+1 == len(nums)):
                return i
            if(nums[i] > nums[i+1]):
                return i
        
            

solution = Solution()
print(solution.findPeakElement([1,2,3,4]))
