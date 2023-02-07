def hello():
    print("hello hcl")
def call(func):
    temp=func()
    return temp
d=call(hello)
d