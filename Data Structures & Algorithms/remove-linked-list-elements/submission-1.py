# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        def helper(node):
            if not node or not node.next:
                return
            
            if node.next.val == val:
                node.next = node.next.next
                return helper(node)
            
            return helper(node.next)
        
        helper(dummy)

        return dummy.next