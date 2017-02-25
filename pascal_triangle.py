class Solution(object):
    result = [[1]]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        for i in range(numRows-1):
            self.result.append(self.new_row(self.result[i]))
        return self.result

    def new_row(self, old_row):
        row = []
        for i in range(len(old_row)):
            if(i == 0):
                item = old_row[i]
                row.append(item)
            if(i-1 >= 0):
                item = old_row[i] + old_row[i-1]
                row.append(item)
            if(i == (len(old_row)-1)):
                item = old_row[i]
                row.append(item)
        return row

solution = Solution()
print(solution.generate(7))
