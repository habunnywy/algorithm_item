"""
给定一个正整数n,找出所有1到n中，每一位数字都不相同数的个数，例如：当n=13时，返回12 ，因为1-13中，仅有11这一数它两个数字均为1不满足不相同的要求
"""
class Solution:
    def countUniqueNumbers3(self ,start_n:int, n: int) -> int:
        no_repeat_num = 0
        for i in range(start_n,n+1):
            digit_list = [int(digit) for digit in str(i)]
            if len(digit_list) == len(set(digit_list)):
                no_repeat_num += 1

        return no_repeat_num
    def countUniqueNumbers(self,n,use_num = 9,raw = None):
        if use_num == 9:
            raw = n
        if n <= 9:
            return self.countUniqueNumbers3(raw-raw%10,raw)
        length = len(str(n))
        tmp1 = self.count_length(length-1)
        tmp2 = self.countUniqueNumbers(int(str(n)[1:]),use_num=use_num-1,raw=raw)
        return tmp1 + tmp2


    def count_length(self,length,use_num = 9):
        """
        到位数对应lenght个use_num的不重复个数
        """
        if length == 1 :
            return use_num
        elif length == 2:
            return use_num*use_num + self.count_length(1)
        else:
            tmp = use_num
            for _ in range(length-1):
                tmp *= (use_num-_)
            return self.count_length(length-1) + tmp

n = 99
s = Solution()
print(s.countUniqueNumbers(n))
print(s.countUniqueNumbers3(start_n=1,n=n))
