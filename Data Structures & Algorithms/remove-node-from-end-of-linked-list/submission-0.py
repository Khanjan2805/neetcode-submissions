# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      
        # Create a dummy node before the actual head.
        # This makes it easier to handle the case
        # where we have to remove the first node.
        dummy = ListNode(0)
        dummy.next = head

        # Both pointers start from the dummy node.
        slow = dummy
        fast = dummy

        # -----------------------------------------
        # STEP 1: Create a gap of n + 1 nodes
        # between slow and fast.
        # -----------------------------------------
        #
        # We use n + 1 instead of n because we
        # want slow to finally stop at the node
        # BEFORE the node we want to remove.

        for i in range(n + 1):
            fast = fast.next

        # -----------------------------------------
        # STEP 2: Move both pointers together
        # -----------------------------------------
        #
        # Fast and slow now move at the same speed.
        # When fast reaches the end,
        # slow will be at the node BEFORE
        # the node that needs to be removed.

        while fast is not None:
            slow = slow.next
            fast = fast.next

        # -----------------------------------------
        # STEP 3: Remove the node
        # -----------------------------------------
        #
        # slow is standing just before the target.
        #
        # Example:
        #
        # 1 → 2 → 3 → 4
        #     ↑    ↑
        #   slow target
        #
        # We make 2 point directly to 4.

        slow.next = slow.next.next

        # Return dummy.next because dummy itself
        # is not part of our actual linked list.
        return dummy.next
        