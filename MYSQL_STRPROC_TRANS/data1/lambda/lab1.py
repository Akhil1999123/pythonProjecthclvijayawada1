"""add=lambda x,y:x+y
print(add(10,20))

m=lambda a,b:a if (a>b) else b"""
def demo(x):
    return lambda a:a*x
d=demo(5)
print(d(11))