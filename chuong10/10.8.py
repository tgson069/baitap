import calendar
from datetime import datetime
a = int(input("ngay "))
b = int(input("thang "))
c = int(input("nam "))
print(a,"-",b,"-",c)
if calendar.isleap(c) == True:
    print(c,"la nam nhuan")
else:
    print(c,"khong phai nam nhuan")
k=str(calendar.monthrange(c,b))
e=k.strip(")")
d=e.split(",")
print(d[1])
lst=["thu hai","thu ba","thu tu","thu nam","thu sau","thu bay","chu nhat"]
t= calendar.weekday(c,b,a)
print(lst[t])
