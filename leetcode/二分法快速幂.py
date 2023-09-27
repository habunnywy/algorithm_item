def quick_power(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    if n&1==0:
        return quick_power(a**2,n>>1)
    else:
        return quick_power(a**2,n>>1)*a

def quick_power2(a, n):
    result = 1
    base = a
    while n > 1:
        if n & 1==1:
            result=base
        base*=base
        n>>=1
    result*=base
    return result


a=2
n=1000000000
import time
start=time.time()
quick_power(a,n)
end=time.time()
print(end-start)
