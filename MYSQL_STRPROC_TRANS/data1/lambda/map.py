old_price=[22,33,4,5,6,7,8,8]
rs=5
def add_price(no):
    return  no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(list(new_price1))