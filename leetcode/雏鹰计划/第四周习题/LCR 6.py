'''
Z 字形变换

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)<=numRows:
            return s
        z_out_list = [[] for _ in range(numRows)]
        direction = -1
        row_index = 0
        for i,c in enumerate(s):
            z_out_list[row_index].append(c)
            if i%(2*numRows-2)==0 or (i-numRows+1)%(2*numRows-2)==0:
                direction *= -1
            row_index += direction
        z_out_list = [''.join(_) for _ in z_out_list]

        return ''.join(z_out_list)

    def convert2(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n<=numRows:
            return s
        ans = []
        t = 2 * numRows -2 #每个周期元素个数
        for i in range(numRows): # 答案每一行
            for j in range(0,n-i,t): # 每行的每个周期，这样遍历不会超界,遍历每个周期起始下标
                ans.append(s[j+i])
                if i not in [0,numRows-1] and j+t-i < n: #还要保证这一周期起始往后有字符
                    ans.append(s[j+t-i])
        return ''.join(ans)

if __name__ == '__main__':
    s = Solution()
    input_s = 'PAYPALISHIRING'
    numRows = 3
    print(s.convert(input_s,numRows))