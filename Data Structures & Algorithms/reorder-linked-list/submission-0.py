# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        turtle = head
        rabbit = head
        while rabbit.next and rabbit.next.next:
            turtle = turtle.next
            rabbit = rabbit.next.next

        prev = None
        curr = turtle.next
        turtle.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        secondHalf = prev
        headSave = head    
        while secondHalf:
            headNext = head.next

            head.next = secondHalf
            
            tempSecondNext = secondHalf.next 
            secondHalf.next = headNext
            
            head = headNext
            secondHalf = tempSecondNext
