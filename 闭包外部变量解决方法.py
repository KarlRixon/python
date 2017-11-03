def funx():
    x=[8]
    #用列表防止闭包内对外部变量屏蔽
    def funy():
        x[0]*=x[0]
        return x[0]
    return funy()

print(funx())
