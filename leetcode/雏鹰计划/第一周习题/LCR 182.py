'''

某公司门禁密码使用动态口令技术。初始密码为字符串 password，密码更新均遵循以下步骤：

设定一个正整数目标值 target
将 password 前 target 个字符按原顺序移动至字符串末尾
请返回更新后的密码字符串。

示例 1：

输入: password = "s3cur1tyC0d3", target = 4
输出: "r1tyC0d3s3cu"
'''


class Solution:
    def dynamicPassword(self,password: str,target: int) -> str:
        return f'{password[target:]}{password[:target]}'


if __name__=='__main__':
    test_password="s3cur1tyC0d3"
    target=4
    s=Solution()
    print(s.dynamicPassword(test_password,target))
