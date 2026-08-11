class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            # Find middle index
            mid = (low + high) // 2

            # Case 1: Target found
            if nums[mid] == target:
                return mid

            # Case 2: Left half is sorted
            elif nums[low] <= nums[mid]:

                # Check if target lies inside sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Target is in the right half
                else:
                    low = mid + 1

            # Case 3: Right half is sorted
            else:

                # Check if target lies inside sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Target is in the left half
                else:
                    high = mid - 1

        # Target was not found
        return -1  