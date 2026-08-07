from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Minimum possible eating speed
        low = 1

        # Maximum possible eating speed
        high = max(piles)

        # Stores the minimum valid speed
        answer = high

        # Binary Search on eating speed
        while low <= high:

            # Find current eating speed
            mid = (low + high) // 2

            # Total hours required at this speed
            total_hours = 0

            # Calculate hours for every pile
            for pile in piles:

                # ceil(pile / mid) because even
                # 1 banana left requires 1 extra hour
                total_hours += ceil(pile / mid)

            # Current speed works
            if total_hours <= h:

                answer = mid          # Store answer

                high = mid - 1        # Try smaller speed

            # Current speed is too slow
            else:

                low = mid + 1

        return answer
        