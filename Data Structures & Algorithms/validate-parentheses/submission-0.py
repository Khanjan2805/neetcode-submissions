class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:

            # Opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # Closing bracket ')'
            elif ch == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()

            # Closing bracket '}'
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()

            # Closing bracket ']'
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0