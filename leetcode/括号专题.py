def buildTree(inorder,postorder):
    if not inorder or not postorder:
        return None

    root_val=postorder.pop()
    root=TreeNode(root_val)
    inorder_index=inorder.index(root_val)

    root.right=buildTree(inorder[inorder_index+1:],postorder)
    root.left=buildTree(inorder[:inorder_index],postorder)

    return root


def preOrderTraversal(node,result):
    if node:
        result.append(node.val)
        preOrderTraversal(node.left,result)
        preOrderTraversal(node.right,result)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


if __name__=="__main__":
    postorder=list(input().strip())
    inorder=list(input().strip())

    root=buildTree(inorder,postorder)
    result=[]
    preOrderTraversal(root,result)
    print("".join(result))
