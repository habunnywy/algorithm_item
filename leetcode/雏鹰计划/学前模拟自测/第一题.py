



'''
计算面积：

4 10
1 1
2 1
3 1
4 -2
'''










class Solution:

    def get_min_area(self, instructions, stop_point):
        n_instru = len(instructions)
        h = 0
        S = 0
        for i,(x,y) in enumerate(instructions):
            h += y
            if i < n_instru-1 :
                k = instructions[i+1][0]
            else:
                k = stop_point
            S += abs(h) * (k-x)

        return S


if __name__ == "__main__":
    row_count, stop_point = map(int, input().strip().split())
    instructions = [list(map(int, input().strip().split())) for _ in range(row_count)]
    function = Solution()
    result = function.get_min_area(instructions, stop_point)
    print(result)

