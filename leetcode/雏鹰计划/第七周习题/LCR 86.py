from typing import Optional
import time
'''
分隔链表

给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，
使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition0(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        这样内存消耗太大了
        :param head:
        :param x:
        :return:
        '''
        left_node = []
        right_node = []
        node = head
        while node:
            if node.val < x:
                left_node.append(node)
            else:
                right_node.append(node)
            node = node.next

        if left_node and right_node:
            left_node[-1].next = right_node[0]

        if left_node:
            start_node = left_node[0]
        elif right_node:
            start_node = right_node[0]
        else:
            return head

        if left_node:
            node = left_node.pop(0)
            while left_node:
                n = left_node.pop(0)
                node.next = n
                node = n

        if right_node:
            node = right_node.pop(0)
            while right_node:
                n = right_node.pop(0)
                node.next = n
                node = n

        return start_node

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        :param head:
        :param x:
        :return:
        '''
        left_head = ListNode(0)
        right_head = ListNode(0)
        left_node = left_head
        right_node = right_head
        node = head
        while node:
            if node.val < x:
                left_node.next = node
                left_node = left_node.next
            else:
                right_node.next = node
                right_node = right_node.next
            node = node.next

        left_node.next = right_head.next
        right_node.next = None  # 取消掉多余的内存空间


        return left_head.next


if __name__ == '__main__':
    node6 = ListNode(2)
    node5 = ListNode(5, node6)
    node4 = ListNode(2, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(4, node3)
    head = ListNode(1, node2)
    s = Solution()
    print(s.partition(head,3).val)
