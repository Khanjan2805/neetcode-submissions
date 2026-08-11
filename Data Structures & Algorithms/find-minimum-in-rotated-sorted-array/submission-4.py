class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            # Left half is unsorted / minimum is on the right
            if nums[mid] > nums[high]:
                low = mid + 1

            # Minimum is at mid or somewhere on the left
            else:
                high = mid

        # low == high, so this index contains the minimum
        return nums[low]


        