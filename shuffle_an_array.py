import random

class Solution(object):

    _orig = []
    _permutation = []

    def __init__(self, nums):
        """        
        :type nums: List[int]
        :type size: int
        """
        self._orig = nums[:]
        for i in range(len(nums)):
            index = random.randrange(len(nums))
            self._permutation.append(nums[index])
            nums.pop(index)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return self._permutation
        
# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3,2,5])
print(obj.reset())
print(obj.shuffle())
