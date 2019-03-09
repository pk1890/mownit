#liczy 1/e^x

import math

def fact(x :int):
    return 1 if x == 0 else fact(x-1)

def exp(x:int, acc: int):
    res = 0
    for i in range (0, acc):
        res += (x**i)/fact(i)

    return res

def bttrexp(x:int, acc: int):
    res = 0
    if x < 0: return (1/bttrexp(-x, acc))
    for i in range (0, acc):
        res += (x**i)/fact(i)

    return res

print("Gorsze: ", exp(-3, 10), "Lepsze: ", bttrexp(-3, 10))
