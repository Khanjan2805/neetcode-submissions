# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # -------------------------------
        # STEP 1: Find the middle
        # -------------------------------
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the middle node
        middle = slow


        # -------------------------------
        # STEP 2: Split the list
        # -------------------------------
        # second will point to the first node
        # of the second half
        second = middle.next

        # Break the connection between the two halves
        middle.next = None


        # -------------------------------
        # STEP 3: Reverse the second half
        # -------------------------------
        prev = None
        current = second

        while current is not None:

            # Save the next node before changing the link
            next_node = current.next

            # Reverse the link
            current.next = prev

            # Move prev forward
            prev = current

            # Move current forward
            current = next_node

        # prev is now the head of reversed second half
        second = prev


        # -------------------------------
        # STEP 4: Merge both halves
        # -------------------------------
        first = head

        while second is not None:

            # Save next nodes before changing links
            first_next = first.next
            second_next = second.next

            # Put one node from second after first
            first.next = second

            # Connect second to the next node of first
            second.next = first_next

            # Move first forward
            first = first_next

            # Move second forward
            second = second_next
        