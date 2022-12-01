r=int(input("nhap r "))
a=int(input("nhap a "))
b=int(input("nhap b "))
listz=[r,r,a,b+a]
listb=[(r*3.14),6.28,b,2]
list2=list(map(lambda i1,i2: i1*i2,listz,listb))
print(list2)
