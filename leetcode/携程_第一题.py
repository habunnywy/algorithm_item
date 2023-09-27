import sys
from itertools import permutations
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True


def valid_paixu(num):
    for i in range(len(num)-1):
        if is_prime(num[i]+num[i+1]):
            return False
    return True
def count_non_prime(n):
    total=0
    for n in permutations(range(1,n+1)):
        if valid_paixu(n):
            total+=1
    return total
n=int(input())
count=count_non_prime(n)
print(count)
