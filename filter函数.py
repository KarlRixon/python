def odd(x):
    return x%2
temp=range(10)
show=filter (odd,temp)
print(list(show))
#filter用于过滤出按规定规则运算后非假的结果
print('应用lmabda表达式：')
print(list(filter(lambda x:x%2,range(10))))
