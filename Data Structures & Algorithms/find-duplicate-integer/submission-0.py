class Solution:
    def findDuplicate(self, nums):

        # Both pointers start from index 0
        slow = 0
        fast = 0

        # STEP 1: Find a meeting point inside the cycle
        while True:

            # Slow moves one step
            slow = nums[slow]

            # Fast moves two steps
            fast = nums[nums[fast]]

            # If they meet, a cycle exists
            if slow == fast:
                break

        # STEP 2: Find the beginning of the cycle
        slow = 0

        while slow != fast:

            # Both now move one step
            slow = nums[slow]
            fast = nums[fast]

        # The meeting point is the duplicate number
        return slow