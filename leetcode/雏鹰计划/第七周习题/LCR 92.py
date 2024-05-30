from typing import Optional
from typing import List
'''
反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 入栈加出栈
        node_stack = []
        before_node = None
        after_node = None
        tmp_node = ListNode(0,head)

        node = tmp_node
        for _ in range(left-1):
            node = node.next

        before_node = node

        for _ in range(left,right+1):
            node = node.next
            node_stack.append(node)
        else:
            node = node.next

        after_node = node

        before_node.next = node_stack[-1]


        node = node_stack.pop(-1)
        while node_stack:
            n = node_stack.pop(-1)
            node.next = n
            node = n
        else:
            node.next = after_node

        return tmp_node.next

if __name__ == '__main__':
    node5 = ListNode(5)
    node4 = ListNode(4,node5)
    node3 = ListNode(3,node4)
    node2 = ListNode(2,node3)
    head = ListNode(1,node2)

    s = Solution()
    print(s.reverseBetween(head,2,4).val)