import math
a = int(input("ax^2 nhap a "))
b = int(input("bx nhap b "))
c = int(input("c nhap c "))
if a == 0:
    print("ax^2+bx+c=0 co nghiem =",-c/b)
elif b*b-4*a*c>0  :
    print("phuong trinh co 2 nghiem ")
    print("x1=",(-b-math.sqrt(b*b-4*a*c))/(2*a))
    print("x2=",(-b+math.sqrt(b*b-4*a*c))/(2*a))
elif b*b-4*a*c==0 :
    print("phuong trinh co 1 nghiem")
    print("x=",-b/(2*a))
else:
    print("phuong trinh vo nghiem")
