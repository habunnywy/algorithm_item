letters = 'abcdefghijklmnopqrstuvwxyz'
def str_transform(str):
    return ''.join(sorted(str))

str1 = 'abcda'
print(str_transform(str1))