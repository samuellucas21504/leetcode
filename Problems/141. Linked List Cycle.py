# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        ahead = head
        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

            if ahead == head:
                return True

        return False
