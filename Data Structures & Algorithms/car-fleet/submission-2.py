class Solution:
    def carFleet(self, target, position, speed):

        # Combine position and speed
        cars = list(zip(position, speed))

        # Sort by position
        cars.sort()

        # Stores arrival time of each fleet
        stack = []

        # Traverse from nearest car to target
        for i in range(len(cars) - 1, -1, -1):

            # Time taken by current car
            time = (target - cars[i][0]) / cars[i][1]

            # If no fleet exists OR current car cannot catch the fleet ahead
            if not stack or time > stack[-1]:
                stack.append(time)

            # Else:
            # Current car joins the fleet ahead
            # Do nothing

        # Number of fleets
        return len(stack)