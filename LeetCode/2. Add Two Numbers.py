# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ = ''
        l2_ = ''
        while l1 :
            l1_ += str(l1.val)
            l1 = l1.next
        while l2 :
            l2_ += str(l2.val)
            l2 = l2.next
        result = str(int(l1_[::-1]) + int(l2_[::-1]))[::-1]
        l_head = None
        for i in result:
            if not l_head:
                l_head = ListNode(int(i))
                l_ = l_head
            else:
                l_.next = ListNode(int(i))
                l_ = l_.next
        return l_head

