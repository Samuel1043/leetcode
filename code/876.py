# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        N=0
        node=head
        while node:
            node=node.next
            N+=1
        N=N//2
        node=head
        while N>0:
            node=node.next
            N-=1
        return node