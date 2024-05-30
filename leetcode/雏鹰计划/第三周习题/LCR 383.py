'''
383. 赎金信

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。


'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransom_sort = sorted(ransomNote)
        # magazine_sort = sorted(magazine)
        for s in set(ransomNote):
            if ransomNote.count(s)>magazine.count(s):
                return False
        return True

if __name__ == '__main__':
    s1 = "aa"
    s2 = "aab"
    s = Solution()
    print(s.canConstruct(s1,s2))