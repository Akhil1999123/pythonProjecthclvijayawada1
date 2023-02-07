def outer():
    print("hello from outer-function")
    def inner():
        print("hello from inner function")
    inner()
d=outer()