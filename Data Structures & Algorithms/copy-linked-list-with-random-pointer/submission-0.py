"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        # This dictionary connects:
        # original node → new copied node
        node_copy = {}

        # --------------------------------
        # STEP 1: Create all new nodes
        # --------------------------------

        current = head

        while current is not None:

            # Make a completely new node
            copied_node = Node(current.val)

            # Remember which copy belongs to which original node
            node_copy[current] = copied_node

            # Go to next original node
            current = current.next


        # --------------------------------
        # STEP 2: Connect next and random
        # --------------------------------

        current = head

        while current is not None:

            # Get the copy of the current node
            copied_node = node_copy[current]

            # Connect the copied next pointer
            copied_node.next = node_copy.get(current.next)

            # Connect the copied random pointer
            copied_node.random = node_copy.get(current.random)

            # Move to next original node
            current = current.next


        # Return the copy of head
        return node_copy.get(head)
        