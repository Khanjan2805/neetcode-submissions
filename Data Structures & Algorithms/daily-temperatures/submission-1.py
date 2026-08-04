class Solution:
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)

        answer = [0] * n

        stack = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1):

            # Remove all temperatures
            # smaller or equal to current temperature
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # If stack is not empty,
            # top is next warmer day
            if stack:
                answer[i] = stack[-1] - i

            # Push current day's index
            stack.append(i)

        return answer
        