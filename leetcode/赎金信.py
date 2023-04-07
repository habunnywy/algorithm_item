'''
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。

'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        "用字典分别统计magazine和ransomNote里面的字符个数，若ransomNote的各字符出现次数均小于magazine则True"
        if len(magazine)<len(ransomNote):
            return False
        ran_dict={}
        mag_dict={}
        for s in ransomNote:
            if s not in ran_dict.keys():
                ran_dict[s]=1
            else:
                ran_dict[s]+=1
        for s in magazine:
            if s not in mag_dict.keys():
                mag_dict[s]=1
            else:
                mag_dict[s]+=1
        for k in ran_dict.keys():
            if k not in mag_dict.keys():
                return False
            else:
                if ran_dict[k]>mag_dict[k]:
                    return False
        return True

ransomNote = "aa"
magazine = "aab"
s=Solution()
b=s.canConstruct(ransomNote,magazine)
print(b)