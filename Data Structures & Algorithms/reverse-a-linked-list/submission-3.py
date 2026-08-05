class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_recursive(head):
            # Base case: empty list or single node
            if head is None or head.next is None:
                return head
            
            # Recursively reverse the rest of the list
            new_head = reverse_recursive(head.next)
            
            # Reverse the link between current node and the next node
            head.next.next = head
            head.next = None
            
            return new_head
        
        return reverse_recursive(head)