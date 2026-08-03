class Solution:
    def trap(self, height):

        # Left pointer starts from beginning
        left = 0

        # Right pointer starts from end
        right = len(height) - 1

        # Highest wall seen from left
        leftMax = 0

        # Highest wall seen from right
        rightMax = 0

        # Stores total trapped water
        water = 0

        # Continue until pointers meet
        while left < right:

            # If left wall is smaller
            if height[left] < height[right]:

                # Update the highest wall seen from left
                if height[left] >= leftMax:
                    leftMax = height[left]

                # Otherwise water can be trapped
                else:
                    water += leftMax - height[left]

                # Move left pointer
                left += 1

            # If right wall is smaller or equal
            else:

                # Update the highest wall seen from right
                if height[right] >= rightMax:
                    rightMax = height[right]

                # Otherwise water can be trapped
                else:
                    water += rightMax - height[right]

                # Move right pointer
                right -= 1

        return water
        