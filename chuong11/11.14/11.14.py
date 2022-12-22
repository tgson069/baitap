danhba={}
sdt=open("sdt.txt","r+")
a=sdt.read()
lst=a.split(",")
b=len(lst)
m=1
i=2
phay=","
while m<b:
    d=str(lst[(m-1)])
    h=str(lst[(i-1)])
    danhba[d]=h
    m+=2
    i+=2
print("danh sách trong danh bạ ",danhba.keys())
h=int(input("1: tra danh bạ,2: thêm số vào danh bạ,3: xóa số,0: kết thúc"))
while (h == 1)or(h==2)or(h==3) :
    while h==3:
         sx=""
         sx=str(input("nhap ten muon xoa"))
         del danhba[sx]
         h=int(input("1: tra danh bạ,2: thêm số vào danh bạ,3: xóa số,0: kết thúc"))
    while h==2:
         s=1
         ten=""
         so=""
         ten=str(input("nhập tên trong danh bạ "))
         so=str(input("nhập số điện thoại "))
         ktr1=(ten)in danhba
         if (ktr1 == True):
             print("tên hoặc số đã có trong danh bạ bạn có muốn đổi tên hoặc số đã có ")
             s=int(input("1:có,2:không "))
         if s==1:
            danhba[ten]=so
            h=int(input("1: tra danh bạ,2: thêm số vào danh bạ,3: xóa số,0: kết thúc"))
    while h==1:
         tra=str(input("nhập search name "))
         m=(tra)in danhba
         if m == False:
            print("tên không có trong danh bạ")
            h=int(input("1: tra danh bạ,2: thêm số vào danh bạ,3: xóa số,0: kết thúc"))
         else:
            print("số điện thoại của",tra,"là",danhba[tra])
            h=int(input("1: tra danh bạ,2: thêm số vào danh bạ,3: xóa số,0: kết thúc"))
print(danhba)
sdt.seek(0)
sdt.truncate(0)
for i in danhba:
    new=danhba[i]
    new=phay+new
    i=phay+i
    sdt.write(i)
    sdt.write(new)
sdt.closed
