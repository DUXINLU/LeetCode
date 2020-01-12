# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_=l1
        l2_=l2
        s1=""
        s2=""
        while True: #l1
            s1=s1+str(l1.val)
            if  l1.next:
                l1=l1.next
            else:
                break
        while True: #l2
            s2=s2+str(l2.val)
            if  l2.next:
                l2=l2.next
            else:
                break
        n1=int(s1[::-1])
        n2=int(s2[::-1])
        sum_l=list(str(n1+n2))
        sum_l.reverse()
        print(sum_l)
        l_res=ListNode(int(sum_l[0]))
        _=l_res
        for i in sum_l[1:]:
            _.next=ListNode(int(i))
            _=_.next
        return l_res
