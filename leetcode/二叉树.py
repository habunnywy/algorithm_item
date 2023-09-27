import numpy as np
class node():
    def __init__(self):
        self.value=None
        self.lchild=None
        self.rchild=None
    def visit(self):
        print(self.value)

class Binary_tree():
    def __init__(self):
        """
        node_number:结点个数
        node_memory:结点的存储空间
        stack:模拟堆栈空间
        """
        self.node_number=0
        self.node_memory=[]
        self.stack=[]

    def create_full_tree(self,height=3):
        """
        创建高度为height的满二叉树
        :param height: 树的高度/深度
        :return: None
        """
        self.node_number=np.power(2,height)-1
        if height==0:
            return
        for i in range(0,self.node_number): #所有节点入存储空间
            temp_node=node()
            temp_node.value=i
            if i !=0:
                if self.node_memory[(i-1)//2].lchild==None:
                    self.node_memory[(i-1)//2].lchild=temp_node
                else:
                    self.node_memory[(i-1)//2].rchild=temp_node
            self.node_memory.append(temp_node)

    def create_complete_tree(self,node_num=7):
        self.node_number=node_num
        temp_height=np.log2(node_num)
        height=int(np.ceil(temp_height))
        if temp_height-height==0:
            self.create_full_tree(height=height)
            print('ok')
        else:
            self.create_full_tree(height=height-1)
            for i in range(0,node_num-np.power(2,height-1)+1):
                temp_node=node()
                temp_node.value=i
                if i !=0:
                    """
                    父节点没有左子树就分配右子树
                    """
                    if self.node_memory[(i-1)//2].lchild==None:
                        self.node_memory[(i-1)//2].lchild=temp_node
                    else:
                        self.node_memory[(i-1)//2].rchild=temp_node
                self.node_memory.append(temp_node)

    def pre_order(self):
        """
        前序遍历，每一个子树都是根-左-右(DLR),访问后入栈
        :return:None
        """
        p=self.node_memory[0]
        while(p or len(self.stack)!=0):
            if p:
                p.visit()
                self.stack.append(p)
                p=p.lchild
            else:
                p=self.stack.pop()
                p=p.rchild

    def in_order(self):
        """
        中序遍历，每一个子树都是左-根-右(LDR),出栈时访问
        :return:None
        """
        p=self.node_memory[0]
        while(p or len(self.stack)!=0):
            if p:
                self.stack.append(p)
                p=p.lchild
            else:
                p=self.stack.pop()
                p.visit()
                p=p.rchild

    def post_order(self):
        """
        后序遍历
        :return:None
        """
        if self.node_number==0:
            return
        p=self.node_memory[0]
        pre=None #通过判断右子树是否已经访问完毕，来决定是否pop出当前结点
        while(p or len(self.stack)!=0):
            if p:
                self.stack.append(p)
                p=p.lchild
            else:
                p=self.stack[-1] #查看栈顶元素而不是pop出来
                if p.rchild==None or pre==p.rchild:
                    p=self.stack.pop()
                    p.visit()
                    pre=p
                    p=None #既然进来了，就表明右子树都遍历完了，为了防止重复遍历，故设为None
                else:
                    p=p.rchild




tree=Binary_tree()
tree.create_full_tree(height=2)
tree.post_order()
tree.create_complete_tree(7)