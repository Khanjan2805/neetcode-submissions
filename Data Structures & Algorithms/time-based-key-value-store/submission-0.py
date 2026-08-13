class TimeMap:

    def __init__(self):
        # Dictionary:
        # key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        # If key is new, create an empty list
        if key not in self.store:
            self.store[key] = []

        # Timestamps come in increasing order,
        # so simply append.
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        # If key doesn't exist
        if key not in self.store:
            return ""

        arr = self.store[key]

        low = 0
        high = len(arr) - 1

        answer = ""

        # Binary Search
        while low <= high:

            mid = (low + high) // 2

            # Exact timestamp found
            if arr[mid][0] == timestamp:
                return arr[mid][1]

            # Current timestamp is smaller
            # It can be our answer, so go right
            elif arr[mid][0] < timestamp:
                answer = arr[mid][1]
                low = mid + 1

            # Current timestamp is greater
            # Search on left side
            else:
                high = mid - 1

        return answer
        
