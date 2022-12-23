import os
path=""
lsthoadon={}
hoadon=open("hoadon.txt","r+",encoding="utf-8") 
def themhoadon(lsthoadon):
    while True:
        sohoadon=str(input("nhap so hoa don "))
        ngayhoadon=input("ngay hoa don")
        hotenkhach=(input("ho ten khach hang "))
        diachi=(input("dia chi khach hang "))
        quan=input("nhap quan ")
        sdt=input("nhap so dien thoai ")
        tongtien=int(input("nhap tong tien "))
        tamung=int(input("tam ung "))
        conlai=(tongtien-tamung)
        lsthoadon.append({"sohd":sohoadon,"ngayhd":ngayhoadon,"hoten":hotenkhach,
        "diachi": diachi,"quan":quan,"sodienthoai":sdt,"tong tien":tongtien,"tam ung":tamung,"conlai":conlai})
        tt=input("tiep tuc hay khong ")
        if tt!=1:
            break
themhoadon(lsthoadon)



