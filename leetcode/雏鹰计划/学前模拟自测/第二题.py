




'''
简易校验和算法

test:
in:
68 75 61 77 65 69
out:
0D1C9E88

in:
61 62 63 64 32 30 31 32 4C 61 62
out:
1F3330A9
'''
from functools import reduce
import operator
class Solution:
    def simple_check_sum(self, input_str: str) -> str:
        # 在此添加你的代码
        tmp = list(map(lambda x:int(x,16),input_str.split()))
        n = len(tmp)
        if n % 4: # 不能被4整除
            tmp.extend([255] * (4-(n%4)))

        multiple_4 = len(tmp)//4
        if multiple_4 == 1:
            out = ''.join(hex(x)[2:] for x in tmp).upper()
            if out[0] not in ['1','2','3','4','5','6','7','8','9']:
                return f'0{out}'
            else:
                return out

        tmp_group = [int(''.join(hex(x)[2:] for x in tmp[_*4:_*4+4]),16) for _ in range(multiple_4)]

        out = reduce(operator.xor,tmp_group)
        out = hex(out)[2:].upper()

        if out[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return f'0{out}'
        else:
            return out


if __name__ == "__main__":
    input_str = str(input().strip())
    function = Solution()
    results = function.simple_check_sum(input_str)
    print(results)
