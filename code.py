def rev(x,y):
    if y==0:
        return x
    else:
        return rev(x*10+y%10,y//10)
y=int(input("enter any thing:"))
print(rev(0,y))
