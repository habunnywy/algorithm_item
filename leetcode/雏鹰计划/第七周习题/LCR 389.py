'''
给定两个字符串 s 和 t ，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

字符串问题，注意字符串也是数字！！！
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
        t_dict = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}

        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1

        for c in s_dict.keys():
            if s_dict[c] != t_dict[c]:
                return c

    def findTheDifference2(self, s: str, t: str) -> str:
        s_sum = sum(map(ord,s))
        t_sum = sum(map(ord,t))
        return chr(t_sum-s_sum)

    def findTheDifference3(self, s:str, t:str) -> str:
        s = s + 'A'
        sum = 0
        for i, j in zip(s, t):
            sum += ord(j)
            sum -= ord(i)
        sum += ord('A')
        return chr(sum)



if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    solution = Solution()
    print(solution.findTheDifference3(s,t))