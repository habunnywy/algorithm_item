"""
原问题
一张纸从下往上对折之后，出现一条折痕，该折痕凸起向下，所以叫“下折痕”，反之如果摊开之后，凸起向上，则叫上折痕。
如果一张纸从下往上对折两次，则折痕为 [下，下，上]
问：
给定整数num，表示这张纸按照从下往上折叠的方式折叠num次，摊开之后，从上往下的折痕方向顺序是什么？
如：
num = 2
结果为：下下上
"""
class node():
    def __init__(self,value=None,lchild = None,rchild = None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

    def generate(self):
        self.lchild = node(False,None,None)
        self.rchild = node(True,None,None)

    def generate_tree(self,depth):
        """
        :param depth: 所需要的深度，也是递归中要考虑变动的层数
        :return:
        """
        if depth == 0:
            return
        # 每一次递归需要做的
        self.generate() #本节点生成
        self.lchild.generate_tree(depth-1) #左节点生成
        self.rchild.generate_tree(depth-1) #右节点生成

    def __str__(self):
        return '上' if self.value else '下'

    def in_order(self):
        if self.lchild == None:
            return
        self.lchild.in_order()
        print(self)
        self.rchild.in_order()

Root_node = node(value = False)
Root_node.generate_tree(3)
Root_node.in_order()