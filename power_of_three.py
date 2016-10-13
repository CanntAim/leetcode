class Solution(object):
    """
    :type n: int
    :rtype: bool
    """
    def isPowerOfThree(self, n):
        if((n ** (1.0/3.0)).is_integer()):
            return True
        else:
            return False

solution = Solution() 
print(solution.isPowerOfThree(27))
print(solution.isPowerOfThree(28))
