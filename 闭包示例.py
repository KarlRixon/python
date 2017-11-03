def funx(x):
    def funy(y):
        return x*y
    return funy

i=funx(8)
print('i=funx(8)')
print('i(5)=',i(5))
print('funx(8)(5)=',funx(8)(5))
