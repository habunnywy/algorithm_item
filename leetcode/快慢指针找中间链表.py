class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head) -> ListNode:
        p,q=head,head
        while (q!=None and q.next!=None):
            p=p.next
            q=q.next.next
        return p
node0=ListNode(6)
node1=ListNode(5,node0)
node2=ListNode(4,node1)
node3=ListNode(3,node2)
node4=ListNode(2,node3)
node5=ListNode(1,node4)

s=Solution()
s_middle=s.middleNode(node5)