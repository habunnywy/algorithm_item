def can_become_palindrome(s):
    transform = {
        #映射轴对称
        "w": '11',
        "v": '1',
        "m": '22',
        "b": '3',
        "d": '3',
        "p": '3',
        "q": '3',
        "n": '2',
        "u": '2',
    }
    new_s = []
    for c in s:
        if c in transform:
            new_s.append(transform[c])
        else:
            new_s.append(c)

    new_s = ''.join(new_s)
    #通过双指针判断是否可以I
    l, r = 0, len(new_s) - 1
    while l<=r:
        if new_s[l] != new_s[r]:
            return "NO"
        l+=1
        r-=1
    return "YES"

n=int(input().strip())
for i in range(n):
    s=input()
    if len(s)<=1:
        print('YES')
    else:
        print(can_become_palindrome(s))