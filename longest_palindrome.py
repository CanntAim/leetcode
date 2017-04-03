class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        middle_odd = 0
        total_even = 0
        for character in s:
            if character not in count:
                count[character] = 1
            else:
                count[character] = count[character] + 1
        for key,value in count.items():
            if value%2 is not 0 and middle_odd is 0:
                middle_odd = value
            elif value%2 is not 0:
                total_even = total_even + value - 1
            else:
                total_even = total_even + value

        return total_even + middle_odd

solution = Solution()
print(solution.longestPalindrome('abcccccdd'))
