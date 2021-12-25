# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        l1_str, l2_str = '', ''
        
        while l1 or l2:
            
            if l1:
                l1_str = str(l1.val) + l1_str
                l1 = l1.next
                
            if l2:
                l2_str = str(l2.val) + l2_str
                l2 = l2.next
                
        total = str(int(l1_str) + int(l2_str))
        
        head = ListNode(int(total[-1]))
        output = head
        
        for i in range(len(total) - 2, -1, -1):
            
            head.next = ListNode(int(total[i]))
            head = head.next
            
        head.next = None
        
        return output