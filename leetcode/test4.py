def can_become_palindrome(s):
    transform = {
        "w": 'vv',
        "m": 'nn',
        "b": 'x',
        "d": 'x',
        "p": 'x',
        "q": 'x',
        "n": 'y',
        "u": 'y',
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