class Solution:
    def threeSum(self, nums):

        # Step 1: Sort the array
        # Sorting helps us use the Two Pointer technique
        # and also makes duplicate handling easy.
        nums.sort()

        # This list will store all valid triplets.
        result = []

        # Step 2: Pick one element at a time.
        # We stop at n-2 because we need at least two more elements.
        for i in range(len(nums) - 2):

            # Step 3: Skip duplicate values of i.
            # Example:
            # [-1, -1, 0, 1]
            # If we already processed the first -1,
            # there is no need to process the second -1.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 4: Two Pointers
            left = i + 1
            right = len(nums) - 1

            # Step 5: Search for the remaining two numbers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # We found a valid triplet
                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate values from left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values from right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Sum is too small
                # Increase it by moving left pointer
                elif total < 0:
                    left += 1

                # Sum is too large
                # Decrease it by moving right pointer
                else:
                    right -= 1

        return result
        