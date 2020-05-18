import math

def isOdd(n):
    return False if n % 2 == 0 else True

def isNaturalSqr(n):
    return True if math.sqrt(n) - math.floor(math.sqrt(n)) == 0 else False

def getXY(s, n):
    l = math.pow(s, 2) - n
    return isNaturalSqr(l) and (s, int(math.sqrt(l))) or getXY(s + 1, n)

def getAB(x, y):
    return x + y, x - y

print("Insert number:")
N = int(input())
assert (N > 1 and isOdd(N)), "Unexpected value!"

x, y = getXY(abs(math.ceil(math.sqrt(N))), N)
a, b = getAB(x, y)

print("Result:", a, b)
