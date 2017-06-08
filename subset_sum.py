class Solution(object):
    def subset_sum(self, nums, target):
        return self.opt(nums,len(nums)-1, target, [])

    def opt(self, nums, index, weight, answer):
        if index < 0 and weight is 0:
            return answer
        elif index < 0 and weight is not 0:
            return []
        else:
            return self.hit(
            self.opt(nums, index-1, weight, answer[:]),
			self.opt(nums, index-1, weight-nums[index], self.add(answer[:], nums[index])))

    def hit(self, a, b):
        if a:
            return a
        elif b:
            return b
        else:
            return []

    def add(self,array,element):
        array.append(element)
        return array

print(Solution().subset_sum([2,1,1,1], 3))
