def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

result=fib(35)
print('共有%d只小兔崽子出生'%result)
