class Solution(object):
    def containsNearbyAlmostDuplicateNaive(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # O(n^2)
        for index_x,item_x in enumerate(nums):
            for index_y,item_y in enumerate(nums):
                if(k >= abs(index_x-index_y)
                and t >= abs(item_x-item_y)
                and index_x-index_y != 0):
                    return True
        return False

    def containsNearbyAlmostDuplicateBetter(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        # O(n+n+n*log(n)) or O(n*log(n))

        # O(n)
        scratch = list()
        for index,item in enumerate(nums):
            scratch.append((index,item))

        # Timsort is O(n*log(n))
        scratch.sort(key=lambda x: x[1])

        # O(n)
        for index in range(0,len(scratch)-1):
            if(t >= scratch[index+1][0] - scratch[index][0]
            and k >= scratch[index+1][1] - scratch[index][1]):
                return True
        return False



Solution = Solution()
print(Solution.containsNearbyAlmostDuplicateNaive([1000,200,300,8,40,20,1,6,13,420],1,1))
print(Solution.containsNearbyAlmostDuplicateBetter([1000,200,300,8,40,20,1,6,13,420],1,1))
