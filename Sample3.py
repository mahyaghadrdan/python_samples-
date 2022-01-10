def factorial(a):
    b = 1
    for i in range(1,a+1):
        b = b*i
    return b

def power(a,b):
    m = 1
    for i in range(b):
        m = m*a
    return m

f1 = factorial(3)
print(f1)
f2 = factorial(4)
print(f2)
f3 = power(f1,f2)
print(f3)
