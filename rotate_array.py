class Solution(object):
    cur = 0
    replace = None
    move = None
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def index(i):
            if i > len(nums)-1:
                return i-len(nums)
            else:
                return i

        self.replace = nums[0]
        self.move = nums[0]
        for x in range(0, len(nums)):
            x = index(self.cur)
            y = index(self.cur + k)

            self.move = self.replace
            self.replace = nums[y]

            nums[y] = self.move
            self.cur = y

        print(nums)

Solution().rotate([1,2,3,4,5,6,7,8],0)
