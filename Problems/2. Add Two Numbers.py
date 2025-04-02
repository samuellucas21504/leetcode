# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode()
        cur = first
        leading = 0

        while l1 != None or l2 != None:
            if l1 != None:
                d1 = l1.val
            else:
                d1 = 0
            if l2 != None:
                d2 = l2.val
            else:
                d2 = 0

            t = d1 + d2 + leading
            s = t % 10
            leading = t // 10

            cur.next = ListNode(s)

            cur = cur.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if leading > 0:
            cur.next = ListNode(leading)

        return first.next