class Solution:
    def isValid(self, s: str) -> bool:
        stack="."
        for i in s:
            if i=='{':
                stack+=i
            if i=='}':
                if stack[-1]=='{':
                    stack=stack[:-1]
                else:
                    stack+=i
            if i=='(':
                stack+=i
            if i==')':
                if stack[-1]=='(':
                    stack=stack[:-1]
                else:
                    stack+=i
            if i=='[':
                stack+=i
            if i==']':
                if stack[-1]=='[':
                    stack=stack[:-1]
                else:
                    stack+=i
        #print(stack)
        if stack==".":
            return True
        return False
