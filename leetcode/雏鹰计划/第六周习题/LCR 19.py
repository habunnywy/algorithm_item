from typing import List
from typing import Optional
'''
19. 删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点.
示例 1:

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]


示例 2：

输入：head = [1], n = 1
输出：[]


示例 3：

输入：head = [1,2], n = 1
输出：[1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        node_num = 0
        node = head
        while node:
            node_num += 1
            node = node.next

        # 删除第一个值时，因为没有前置节点
        if node_num == n:
            return head.next

        node = head
        for _ in range(node_num-n-1):
            node = node.next

        node.next = node.next.next

        return head

