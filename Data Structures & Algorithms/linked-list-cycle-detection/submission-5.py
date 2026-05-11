# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        while rabbit and rabbit.next:
            if rabbit.next.next == None:
                return False    
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        return False            
