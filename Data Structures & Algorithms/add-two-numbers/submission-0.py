# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node to start our new list
        dummy = ListNode(0)
        current = dummy

        # Carry from previous addition
        carry = 0

        # Move through both lists
        while l1 or l2:

            # Get values from both lists
            # If one list is finished, use 0
            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            # Add both values and carry
            total = val1 + val2 + carry

            # Get the digit for our new node
            digit = total % 10

            # Get carry for next addition
            carry = total // 10

            # Add the new digit to our result list
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # If carry is still left, add it
        if carry:
            current.next = ListNode(carry)

        # Return the actual result list
        return dummy.next
        