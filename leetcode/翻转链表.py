# 定义链表结点
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# 定义链表
class LinkList(object):
    def __init__(self):
        self.head = None

    # 添加结点
    def add(self,val):
        node=Node(val)
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next != None:
                cur=cur.next
            cur.next=node


    # 打印链表
    def print(self):
        cur = self.head
        while cur != None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    # 三指针翻转链表
    def reverse(self):
        pre = None
        cur = self.head

        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        self.head = pre
    # 递归翻转链表
    def reverse2(self,head):
        if head.next == None:
            self.head = head
            return
        self.reverse2(head.next) #返回最后一个节点的调用者就是倒数第二个节点
        head.next.next = head
        head.next = None
        return


# 测试
if __name__ == '__main__':
    # 创建链表
    linklist = LinkList()
    # 添加结点
    for i in range(1, 6):
        linklist.add(i)
    # 打印链表
    linklist.print()
    # 翻转链表
    linklist.reverse()
    linklist.reverse2(linklist.head)
    # 打印链表
    linklist.print()