import os
path=""
lsthoadon=[]
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
        return
themhoadon(lsthoadon)        
def inhoadon(lsthoadon):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format("sohd","ngayhd","hoten","diachi","quan","sodienthoai","tongtien","tamung","conlai"))
    for i in lsthoadon:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(i["sohd"],i["ngayhd"],i["hoten"],i["diachi"],i["quan"],i["sodienthoai"],i["tong tien"],i["tam ung"],i["conlai"]))
    return
inhoadon(lsthoadon)


