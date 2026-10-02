# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       
        # Both pointers start at the head
        slow = head
        fast = head

        # Fast moves two steps, so check that both exist
        while fast is not None and fast.next is not None:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # Fast reached the end, so there is no cycle
        return False
        