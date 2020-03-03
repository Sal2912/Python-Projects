n1 = int(input())
n2 = int(input())
if n1>n2:
    small = n2
else:
    small = n1


def gdc():
    for i in range(1, small+1):
        if n1%i == 0 and n2%i == 0:
            gcd1 = i
    return gcd1

print(gdc())


def lmc():
    lcm1 = int((n1*n2)/gdc())
    return lcm1
print(lmc())
