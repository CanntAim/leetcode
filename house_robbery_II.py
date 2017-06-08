class Solution(object):
    maximum = 0
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.decide(0, 0, [], nums)
        return self.maximum

    def decide(self, current, total, grabbed, nums):
        if(total > self.maximum):
            if(not(grabbed[0] == 0 and grabbed[-1] == (len(nums)-1))):
                self.maximum = total
        if(current > len(nums)-1):
            return 0
        self.decide(current+2,total+nums[current], list(self.add(grabbed, current)), nums)
        self.decide(current+1,total, list(grabbed), nums)

    def add(self,array,element):
        new_array = list(array)
        new_array.append(element)
        return new_array

solution = Solution()
print(solution.rob([6000000,20,100,500000,300,1000]))
