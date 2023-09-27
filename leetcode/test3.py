import sys
"""
小欧拿到一个数组a，她每次随机选择一个元素，然后将该元素及其后缀全部删除。
已知第i个元素被选到的概率为a[i]/sum(a)，其中sum(a)表示数组a所有元素之和。
请返回将数组全部删完的期望次数
输入示例:
2
1 3
输出：
1.75
"""

if __name__ == '__main__':
    # 读取每一行
    line = sys.stdin.readline().strip().split()
    n = int(line[0]) # 数组a的长度
    line = sys.stdin.readline().strip().split()
    a = list(map(int, line)) #数组a
    # 计算数组a的和
    sum_a = sum(a)
    # 计算期望次数
    result = 0
    for i in range(n):
        result += a[i]*(n-i)/sum_a+0.25
    print(result)







