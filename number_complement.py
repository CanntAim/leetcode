class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = [int(x) for x in bin(8)[2:]]
        c_a = []
        for b in a:
            if b is 1:
                c_a.append('0')
            else:
                c_a.append('1')

        c_a_s = ''.join(c_a)
        return int(c_a_s, 2)

print(Solution().findComplement(8))
