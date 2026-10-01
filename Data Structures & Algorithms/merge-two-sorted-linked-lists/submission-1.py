

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy node to start our result list
        dummy = ListNode(0)

        # current points to the last node of result
        current = dummy

        # Compare both lists
        while list1 and list2:

            # If list1 value is smaller
            if list1.val <= list2.val:

                # Add list1 node
                current.next = list1

                # Move list1 forward
                list1 = list1.next

            else:

                # Add list2 node
                current.next = list2

                # Move list2 forward
                list2 = list2.next

            # Move current forward
            current = current.next

        # If list1 still has nodes, add them
        if list1:
            current.next = list1

        # Otherwise add remaining list2
        else:
            current.next = list2

        # Return the first node of the merged list
        return dummy.next
        