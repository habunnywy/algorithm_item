#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param mat int整型二维数组
# @param n int整型
# @param m int整型
# @param x int整型
# @return int整型一维数组
#

def binary_find(l, n):
    # l有序 找恰好大于n的下标
    l_mid = l[len(l) // 2]
    if len(l)==1:
        return 1
    if l_mid >= n and l[len(l) // 2 - 1] < n:
        return len(l)//2
    elif l_mid < n:
        return len(l)//2 + binary_find(l[len(l) // 2:], n)
    else:
        return binary_find(l[:len(l) // 2])


class Solution:
    def findElement(self, mat, n: int, m: int, x: int):
        # write code here
        row_first = [mat[_][0] for _ in range(n)]
        ex_row = binary_find(row_first, x)
        need_row = mat[ex_row-1]
        ex_column = binary_find(need_row, x)
        return [ex_row-1, ex_column]

mat=[[1,2,3],[4,5,6]]
n,m,x=2,3,6
s=Solution()
out=s.findElement(mat,n,m,x)
print(out)