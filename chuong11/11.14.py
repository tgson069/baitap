danhba={"son":"098741258"}
sdt=open("sdt.txt","r+")
a=sdt.read()
lst=a.split(",")
b=len(lst)
m=1
i=2
while m<b:
    d=str(lst[(m-1)])
    h=str(lst[(i-1)])
    danhba[d]=h
    m+=2
    i+=2
print("danh sách trong danh bạ /n ",danhba.keys())
h=int(input("tra danh ba =1,them so moi vao danh ba=2,ket thuc=0 "))
while (h == 1)or(h==2) :
    while h==2:
         s=1
         ten=""
         so=""
         ten=str(input("nhap ten trong danh ba "))
         so=str(input("nhap so dien thoai "))
         ktr1=(ten)in danhba
         if (ktr1 == True):
             print("tên hoặc số đã có trong danh bạ bạn có muốn đổi tên hoặc số đã có ")
             s=int(input("co=1,khong=0 "))
         if s==1:
            phay=","
            danhba[ten]=so
            ten=phay+ten
            so=phay+so
            sdt.write(ten)
            sdt.write(so)
         h=int(input("tra danh ba =1,them so moi vao danh ba=2,ket thuc=0 "))
    while h==1:
         tra=str(input("nhap search_name "))
         m=(tra)in danhba
         if m == False:
            print("ten khong co trong danh ba")
            h=int(input("tra danh ba =1,them so moi vao danh ba=2,ket thuc=0 "))
         else:
            print("sdt cua",tra,"la",danhba[tra])
            h=int(input("tra danh ba =1,them so moi vao danh ba=2,ket thuc=0 "))
print(danhba)
sdt.closed