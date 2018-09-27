def fib(n):
    # function Fibonacci Number
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b
fib(10)