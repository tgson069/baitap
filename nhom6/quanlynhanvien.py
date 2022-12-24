from xulythongtin import *
lstnhanvien=[]
path="dsnhanvien.csv"#str(input("nhập file muốn mở :"))
docfile(path,lstnhanvien)
while True:
    print("")
    print("1:thêm nhân viên")
    print("2:in danh sách")
    print("3:lưu danh sách")
    print("4:tìm nhân viên có lương cao nhất")
    print("5:xóa nhân viên theo mã")
    print("6:sắp xếp nhân viên theo mức lương")
    print("0:dừng lại")
    h=int(input("nhập việc muốn làm :"))
    if h==1:
        nhapthongtinnhanvien(lstnhanvien)
    if h==2:
        indanhsach(lstnhanvien)
    if h==3:
        luufile(path,lstnhanvien)
    if h==4:
        maxluong(lstnhanvien)
    if h==5:
        xoanhanvien(lstnhanvien)
    if h==6:
        sapxep(lstnhanvien)
    if h==0:
        k=int(input("bạn đã lưu file chưa ?,bạn có muốn lưu file 1:có,0:không"))
        if k==1:
            luufile(path,lstnhanvien)
            break
        if k==0:
            break
