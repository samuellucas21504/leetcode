# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def reverseList(head):
        new_list = None
        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node

        return new_list
