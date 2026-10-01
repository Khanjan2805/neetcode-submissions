

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        # Previous node starts as None
        prev = None

        # Start from the first node
        current = head

        # Traverse the linked list
        while current is not None:

            # Save the next node
            next_node = current.next

            # Reverse the link
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node

        # Prev is the new head
        return prev