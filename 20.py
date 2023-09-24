class Solution:
    def isValid(self,s):
        stack=[]
        for c in s:
            if len(stack):
                if (c==')' and stack[-1]=='(')\
                or (c==']' and stack[-1]=='[')\
                or (c=='}' and stack[-1]=='{'):
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack)==0
s=Solution()
print(s.isValid('(())'))

