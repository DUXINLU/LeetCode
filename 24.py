# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        head_tmp = ListNode(-1)
        head_tmp.next = head
        t = head_tmp

        while t.next and t.next.next:
            a = t.next
            b = a.next
            t.next = b
            a.next = b.next
            b.next = a
            t = a

        return head_tmp.next