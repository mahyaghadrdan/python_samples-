def factorial(a):
    b = 1
    for i in range(1,a+1):
        b = b*i
    print(b)
    return b
f = factorial(5) + factorial(2)
print(f)