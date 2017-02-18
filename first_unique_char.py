class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = []
        p = {}
        i = 0
        for c in s:
            if c not in p:
                p[c]=i
            if c not in d:
                d.append(c)
            else:
                d.remove(c)
            i=i+1
        return p[d[0]]

solution = Solution()
print(solution.firstUniqChar("leetcode"))
