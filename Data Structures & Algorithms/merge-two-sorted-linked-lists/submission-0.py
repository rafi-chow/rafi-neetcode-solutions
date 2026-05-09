# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = list1
        curr2 = list2
        #0 -> 1
        while curr and curr2:
            nxt1 = curr.next
            nxt2 = curr2.next
            if curr.val <= curr2.val:
                tail.next = curr
                tail = tail.next
                curr = nxt1
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = nxt2
        if curr2:
            tail.next = curr2
        elif curr:
            tail.next = curr
        return dummy.next
