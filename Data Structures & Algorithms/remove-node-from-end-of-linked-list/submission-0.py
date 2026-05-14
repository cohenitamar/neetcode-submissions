# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        nth = head
        newHead = head

        for i in range(n):
            newHead = newHead.next


        if not newHead:
            return head.next

        while newHead.next:
            nth = nth.next
            newHead = newHead.next

        temp = nth.next.next
        nth.next = temp

        return head