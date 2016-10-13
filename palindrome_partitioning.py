class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(set):
            middle = len(set) // 2
            if((len(set) % 2 != 0)):
                for shift in range(0,len(set)/2):
                    if(set[middle-shift-1] != set[middle+shift+1]):
                       return False
                return True
            else:
                for shift in range(0,len(set)/2):
                    if(set[middle-shift-1] != set[middle+shift]):
                        return False
                return True

        result = list()
        in_l = list(s)
        for sub_len in range(1,len(in_l)+1):
            for char_pos in range(0,len(in_l)):
                first = char_pos
                last = char_pos+sub_len
                final = len(in_l)
                if(last < final):
                    set = in_l[first:last]
                    if(in_l[first:last] not in result and is_palindrome(set)):
                        result.append(set)
                        print(set)
                else:
                    set = in_l[first:final]
                    if(in_l[first:final] not in result and is_palindrome(set)):
                        result.append(set)
                        print(set)
        
s = "aabaabcc"
solution = Solution()
print(solution.partition(s))
