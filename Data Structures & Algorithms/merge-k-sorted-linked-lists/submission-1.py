# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        # Fix: Capture the return value of mergeTwoLists
        for i in range(1, len(lists)):
            lists[0] = self.mergeTwoLists(lists[0], lists[i])
            
        return lists[0]


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to hold the start of our new list
        dummy = ListNode()
        tail = dummy
        
        # While both lists still have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move our tail forward to the node we just added
            tail = tail.next
            
        # One list might still have nodes left (e.g., list1 is [1,2], list2 is [1,2,5,6])
        # We just point tail.next to whichever list isn't empty
        tail.next = list1 if list1 else list2
        
        # The real list starts AFTER the dummy node
        return dummy.next    