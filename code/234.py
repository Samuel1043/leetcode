# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        N=0
        node=head
        while node:
            node=node.next
            N+=1
        
        if N==1:
            return True
        
        node=head
        prev_node=None
        
        
        tmp=N//2
        while tmp>0:
            next=node.next
            node.next=prev_node
            prev_node=node
            node=next
            tmp=tmp-1
        if N%2==1:
            node=node.next
        
        while prev_node and node:
            if prev_node.val!=node.val:
                return False
            prev_node=prev_node.next
            node=node.next
            
        # print(prev_node,node)
            
        return prev_node==node==None
        
            
        
        