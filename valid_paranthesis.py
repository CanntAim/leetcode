class Solution(object):
    stack = []
    left = ['{','[','(']
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for c in s:
            if c in self.left:
                self.stack.append(c);
            elif c is ']' and self.stack[-1] is '[':
                self.stack.pop()
            elif c is '}' and self.stack[-1] is '{':
                self.stack.pop()
            elif c is ')' and self.stack[-1] is '(':
                self.stack.pop()
            else:
                return False

        if len(self.stack) is 0:
            return True

print(Solution().isValid('()'))
