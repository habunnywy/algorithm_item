from typing import List
'''
928. 尽量减少恶意软件的传播 II

给定一个由 n 个节点组成的网络，用 n x n 个邻接矩阵 graph 表示。在节点网络中，
只有当 graph[i][j] = 1 时，节点 i 能够直接连接到另一个节点 j。
一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，
那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
我们可以从 initial 中 删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。
请返回移除后能够使 M(initial) 最小化的节点。如果有多个节点满足条件，返回索引 最小的节点。

示例 1：

输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
输出：0
示例 2：

输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
输出：1
示例 3：

输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
输出：1
'''

# class Node:
#
#     def __init_(self, index, is_infect=False):
#         self.index = index
#         self.is_infect = is_infect
from copy import deepcopy
class Infect_graph:

    def __init__(self,connect_list,initial_infect_list):
        self.connect_list = connect_list
        self.infect_list = set(initial_infect_list)

    def spread(self):
        # 使用队列来处理感染传播，这是因为被感染节点只需要考虑传播一次就好了，新的被传播
        # 的节点加入到队列中就行
        queue = list(self.infect_list)

        while queue:
            node_index = queue.pop(0)  # 从队列头部取出一个被感染节点
            node_connect = self.connect_list[node_index] #取出该节点的连接关系
            for i, c in enumerate(node_connect):
                if c and i not in self.infect_list:  # 如果有连接并且该节点未被感染
                    self.infect_list.add(i)
                    queue.append(i)  # 将新感染的节点加入队列

        after_infect_num = len(self.infect_list)
        return after_infect_num


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        original_connect = deepcopy(graph)
        initial = sorted(initial)

        def delete_node(graph, need_delete_index):
            for i in range(len(graph)):
                graph[i][need_delete_index] = 0
                graph[need_delete_index][i] = 0

        # 对每个初始感染节点，删除它以及所有对应的连接
        min_infected = float('inf') # 存储当前最小的感染个数
        result_node = initial[0] # 最小感染个数的节点

        for infect_node in initial:
            graph = deepcopy(original_connect)
            delete_node(graph, infect_node)
            remaining_infect = [node for node in initial if node != infect_node]
            infect_graph = Infect_graph(graph, remaining_infect)
            infected_count = infect_graph.spread()

            if infected_count < min_infected:
                min_infected = infected_count
                result_node = infect_node
            elif infected_count == min_infected:
                result_node = min(result_node, infect_node)

        return result_node

# 下面是并查集方法
    def find(self, uf: List[int], u: int) -> int:
        if uf[u] == u:
            return u
        uf[u] = self.find(uf, uf[u])
        return uf[u]

    def merge(self, uf: List[int], u: int, v: int):
        ru, rv = self.find(uf, u), self.find(uf, v)
        uf[ru] = rv

    def minMalwareSpread2(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        initialSet = [0] * n
        for v in initial:
            initialSet[v] = 1
        uf = [i for i in range(n)]
        for u in range(n):
            if initialSet[u] == 1:
                continue
            for v in range(n):
                if initialSet[v] == 1:
                    continue
                if graph[u][v] == 1:
                    self.merge(uf, u, v)
        infectedBy = [[] for _ in range(n)]
        for v in initial:
            infectedSet = [0] * n
            for u in range(n):
                if initialSet[u] == 1 or graph[u][v] == 0:
                    continue
                infectedSet[self.find(uf, u)] = 1
            for u in range(n):
                if infectedSet[u] == 1:
                    infectedBy[u].append(v)

        count = [0] * n
        for u in range(n):
            if len(infectedBy[u]) != 1:
                continue
            v = infectedBy[u][0]
            for w in range(n):
                if self.find(uf, w) == self.find(uf, u):
                    count[v] += 1
        res = initial[0]
        for v in initial:
            if count[v] > count[res] or (count[v] == count[res] and v < res):
                res = v
        return res




if __name__ == '__main__':
    graph = [[1,1,0,0],[1,1,0,1],[0,0,1,0],[0,1,0,1]]
    initial = [3,0]

    s = Solution()
    print(s.minMalwareSpread(graph,initial))