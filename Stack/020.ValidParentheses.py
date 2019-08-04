class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '({[':
                stack.append(p)
            else:
                if p==')' :
                    if not stack or stack[-1]!='(':
                        return False
                elif p==']':
                    if not stack or stack[-1]!='[':
                        return False
                else:
                    if not stack or stack[-1]!='{':
                        return False
                stack.pop()

        return len(stack)==0
