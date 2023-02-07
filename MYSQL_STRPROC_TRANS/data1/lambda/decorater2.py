def decor(func):
    def inner(name):
        if name=="hcl":
            print("hello hcl with extra function")
        else:
            func(name)
    return inner

@decor

def wish (name):
    print("hello",name)
wish("wipro")
wish("hcl")