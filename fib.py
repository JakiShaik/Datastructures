def fib(n):
    a,b = 1,1
    for _ in range(n):
        a,b = b,a+b
    return b
print(fib(1))
print(fib(10))
