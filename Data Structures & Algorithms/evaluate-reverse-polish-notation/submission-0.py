class Solution:
    def evalRPN(self, tokens):

        # Stack to store numbers
        stack = []

        # Traverse every token
        for token in tokens:

            # If token is '+'
            if token == "+":
                b = stack.pop()          # First pop (right operand)
                a = stack.pop()          # Second pop (left operand)
                stack.append(a + b)      # Push result back

            # If token is '-'
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)      # Important: a - b

            # If token is '*'
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            # If token is '/'
            elif token == "/":
                b = stack.pop()
                a = stack.pop()

                # Division should truncate towards zero
                stack.append(int(a / b))

            # Otherwise it is a number
            else:
                stack.append(int(token))

        # Final answer is the only element left in stack
        return stack[-1]
        