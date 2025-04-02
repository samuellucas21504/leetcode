class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def middleNode(head):
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

        return head
