# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        head = list1
        head2 = list2

        while head and head2:
            nxt = head.next
            nxt2 = head2.next
            if head.val <= head2.val:
                tail.next = head
                tail = tail.next
                head = nxt
            else:
                tail.next = head2
                tail = tail.next
                head2 = nxt2
        if head:
            tail.next = head
        else:
            tail.next = head2
        return dummy.next