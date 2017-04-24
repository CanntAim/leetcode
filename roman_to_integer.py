from exceptions import IndexError

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s)
        value = 0
        for index,i in enumerate(a):
            if index < len(a)-1:
                if i is 'I' and (a[index+1] is not 'V' and a[index+1] is not 'X'):
                    value= value+1
                elif i is 'I':
                    value= value-1
                elif i is 'V':
                    value= value+5
                elif i is 'X' and (a[index+1] is not 'L' and a[index+1] is not 'C'):
                    value= value+10
                elif i is 'X':
                    value= value-10
                elif i is 'L':
                    value= value+50
                elif i is 'C' and (a[index+1] is not 'D' and a[index+1] is not 'M'):
                    value= value+100
                elif i is 'C':
                    value= value-100
                elif i is 'D':
                    value= value+500
                elif i is 'M':
                    value= value+1000
            else:
                if i is 'I':
                    value= value+1
                elif i is 'V':
                    value= value+5
                elif i is 'X':
                    value= value+10
                elif i is 'L':
                    value= value+50
                elif i is 'C':
                    value= value+100
                elif i is 'D':
                    value= value+500
                elif i is 'M':
                    value= value+1000

        return value

print(Solution().romanToInt('XXIV'))
