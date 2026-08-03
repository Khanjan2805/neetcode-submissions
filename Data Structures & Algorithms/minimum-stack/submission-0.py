class MinStack:

    def __init__(self):

        # Main stack stores all values
        self.stack = []

        # Min stack stores the minimum till each position
        self.minStack = []

    def push(self, val: int) -> None:

        # Push value into main stack
        self.stack.append(val)

        # If minStack is empty,
        # first element itself is the minimum
        if not self.minStack:
            self.minStack.append(val)

        else:
            # Compare current value with previous minimum
            # and store the smaller one
            currentMin = min(val, self.minStack[-1])

            self.minStack.append(currentMin)

    def pop(self) -> None:

        # Remove top element from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:

        # Return top element of main stack
        return self.stack[-1]

    def getMin(self) -> int:

        # Top of minStack is always the minimum
        return self.minStack[-1]
        
