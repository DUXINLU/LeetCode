class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


'''
        a,b=headA,headB
        if a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a
'''
