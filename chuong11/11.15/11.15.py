tudien={}
tu=open("tudien.txt","r+",encoding="utf-8")
a=tu.read()
lsttu=a.split(",")
b=len(lsttu)
m=1
i=2
phay=","
while m<b:
    d=str(lsttu[(m-1)])
    h=str(lsttu[(i-1)])
    tudien[d]=h
    m+=2
    i+=2
h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
while (h==1)or(h==2)or(h==3)or(h==4) : 
     while h==1:
        for i in tudien:
            print(i,":",tudien[i])
        h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
     while h==2:
        tra=str(input("nhập từ "))
        m=(tra)in tudien
        if m == False:
            print("không có từ trong từ điển")
            h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
        else:
            print(tra,"có nghĩa là",tudien[tra])
            h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
     while h==3:
        s=1
        anh=""
        viet=""
        anh=str(input("nhập từ tiếng anh cần thêm :"))
        viet=str(input("nhập nghĩa tiếng việt :"))
        ktr1=(anh)in tudien
        if (ktr1 == True):
             print("từ đã có trong danh bạ bạn có muốn nhập tiếp ")
             s=int(input("1:có,2:không "))
             h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
        if s==1:
            tudien[anh]=viet
            h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
     while h==4:
         sx=""
         sx=str(input("nhập tên muốn xóa")) 
         m=sx in tudien
         if m==True:      
            del tudien[sx]
            h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
         else:
            print("không có từ cần xóa trong từ điển")
            h=int(input("bạn muốn làm gì ,1:xem từ điển,2:tra từ,3:thêm từ,4:xóa từ,0:dừng lại"))
tu.seek(0)
tu.truncate(0)
for i in tudien:
    new=tudien[i]
    new=new+phay
    i=i+phay
    tu.write(i)
    tu.write(new)
tu.closed
