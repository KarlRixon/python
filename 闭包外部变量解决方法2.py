def funx():
    x=8
    def funy():
        nonlocal x
        x*=x
        return x
    return funy()

print(funx())
