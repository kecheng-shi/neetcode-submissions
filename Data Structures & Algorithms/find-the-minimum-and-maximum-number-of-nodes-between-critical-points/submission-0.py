# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        max_idx = 0
        min_idx = float('inf')
        min_dis = float('inf')
        max_dis = -1
        idx = 1
        prev = head
        curr = head.next

        while curr and curr.next:
            if prev.val < curr.val > curr.next.val or prev.val > curr.val < curr.next.val:
                if min_idx != float('inf'):
                    min_dis = min(min_dis, idx - max_idx)
                    max_dis = max(max_dis, idx - min_idx)
                min_idx = min(idx, min_idx)
                max_idx = max(idx, max_idx)
            idx += 1
            prev = curr
            curr= curr.next

        return [min_dis, max_dis] if max_dis != -1 else [-1, -1]