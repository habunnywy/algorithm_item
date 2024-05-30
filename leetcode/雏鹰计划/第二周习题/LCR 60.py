from typing import List
'''
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

 

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
 
'''
from itertools import permutations

class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        '''
        暴力做法1
        :param n:
        :param k:
        :return:
        '''

        def getAllPermutation(n):
            if n==1:
                return str(n)
            else:
                new_permutation = []
                last_permu = getAllPermutation(n-1)
                for permu in last_permu:
                    for insert_index in range(n):
                        new_permutation.append(f'{permu[:insert_index]}{n}{permu[insert_index:]}')

                return new_permutation

        permutations_list = getAllPermutation(n)
        permutations_list.sort(key=lambda x:int(x))
        return str(permutations_list[k-1])

    def getPermutation2(self,n: int,k: int) -> str:
        '''
        暴力做法2
        :param n:
        :param k:
        :return:
        '''

        permutations_list = list(permutations([str(_) for _ in range(1,n+1)]))
        permutations_list = [''.join(_) for _ in permutations_list]
        permutations_list.sort(key=lambda x:int(x))
        return str(permutations_list[k-1])

    def getPermutation3(self,n: int,k: int) -> str:
        '''
        数学法
        :param n:
        :param k:
        :return:
        '''

        def factorial(n):
            if n == 0:
                return 1
            else:
                return n*factorial(n-1)

        if n==1:
            return str(1)
        select_num = [str(_) for _ in range(1,n+1)]
        need_permu = []
        k = k-1
        while True:
            if n==1:
                need_permu.append(select_num[0])
                break
            n_fac_next = factorial(n-1)
            need_index = k//n_fac_next
            need_permu.append(select_num[need_index])
            del select_num[k//n_fac_next]
            k = k % n_fac_next
            n -= 1
        return ''.join(need_permu)

if __name__=='__main__':
    n,k = 4,9
    s = Solution()
    print(s.getPermutation3(n,k))
