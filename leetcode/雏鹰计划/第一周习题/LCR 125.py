'''
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
'''
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W+','',s)
        s = re.sub('_+','',s)
        s = s.lower()
        return s==s[::-1]

if __name__ == '__main__':
    s="a_b"
    sol = Solution()
    print(s[::-1])
    print(sol.isPalindrome(s))