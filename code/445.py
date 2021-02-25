# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # cnt=0
    # num1=''
    # num2=''
    # while l1 or l2:
    #     if l1:  
    #         num1=num1+str(l1.val)
    #         l1=l1.next
    #     if l2:
    #         num2=num2+str(l2.val)
    #         l2=l2.next
        
    # total=int(num1)+int(num2)
    # cnt-=1
    # head=ListNode(None)
    # cur=head
    # while total>0 or cnt>=0:
        
    #     cur.next=ListNode(total//(10**cnt))          
    #     cur=cur.next
    #     total=total%(10**cnt)
    #     cnt-=1
    # print(head)
    
    # solved by stack
    num1=[]
    num2=[]
    while l1 or l2:
        if l1:  
            num1.append(l1.val)
            l1=l1.next
        if l2:
            num2.append(l2.val)
            l2=l2.next
        
    cur=ListNode(None)
    
    carry=0
    
    while num1 or num2 or carry:
        cur_num=0
        if num1:
            cur_num+=num1.pop()   
        if num2:
            cur_num+=num2.pop()
        cur_num+=carry
        cur.val=cur_num%10  
        tmp=ListNode(0)
        tmp.next=cur
        cur=tmp
        carry=cur_num//10

    return cur.next

addTwoNumbers(ListNode(5),ListNode(5))