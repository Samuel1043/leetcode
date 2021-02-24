class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head=ListNode(None)
    cur=head
    prev=0
    
    while l1 and l2:
        add=l1.val+l2.val+prev
        if add>=10:
            add-=10
            prev=1
        else:
            prev=0
        cur.next=ListNode(add)
        cur=cur.next
        l1=l1.next
        l2=l2.next
    
    if l1:
        while l1 and prev==1:
            add=l1.val+prev
            if add>=10:
                add-=10
                prev=1
            else:
                prev=0
            cur.next=ListNode(add)
            cur=cur.next
            l1=l1.next
        cur.next=l1
    if l2:
        while l2 and prev==1:
            add=l2.val+prev
            if add>=10:
                add-=10
                prev=1
            else:
                prev=0
            cur.next=ListNode(add)
            cur=cur.next
            l2=l2.next
        cur.next=l2
        
    if prev==1:
        cur.next=ListNode(1)
    
    return head.next