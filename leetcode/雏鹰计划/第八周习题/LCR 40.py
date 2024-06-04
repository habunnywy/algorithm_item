from typing import List
'''
40. 组合总和 II

给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def backtrace(pre_list, remain_target, start):
            if remain_target == 0:
                out.append(list(pre_list)) # 为了防止后续叶节点对其的修改
                return

            peer_num = None
            for i in range(start, len(candidates)):
                tmp = candidates[i]
                if peer_num == tmp:
                    continue
                if tmp > remain_target:
                    break
                pre_list.append(tmp)
                backtrace(pre_list, remain_target - tmp, i + 1)
                pre_list.pop()
                peer_num = tmp


        backtrace([], target, 0)
        return out



if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 4, 5]
    target = 8
    print(solution.combinationSum2(candidates, target))
