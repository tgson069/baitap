import csv
def nhapthongtinnhanvien(lstnhanvien):
    tt=1
    while tt==1:
        manv=input("nhập mã nhân viên :")
        tennv=str(input("nhập tên nhân viên :"))
        luongcb=float(input("nhập lương cơ bản :"))
        namcongtac=float(input("nhập số năm công tác :"))
        if namcongtac < 5:
            phucap=1000000
        elif namcongtac <10:
            phucap=3000000
        elif namcongtac <15:
            phucap=5000000
        elif namcongtac <20:
            phucap=8000000
        else:
            phucap=10000000
        thunhap=luongcb+phucap
        lstnhanvien.append({"manv":manv,"tennv":tennv,"luongcb":luongcb,"namcongtac":namcongtac,"phucap":phucap,"thunhap":thunhap})
        tt=int(input("bạn có muốn tiếp tục nhập 1:có,0:không"))
    return 
def indanhsach(lstnhanvien):
    print('{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format("mã nhân viên","tên nhân viên","lương cơ bản","năm công tác","phụ cấp","thu nhập"))
    for i in lstnhanvien:
        print('{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format(i["manv"],i["tennv"],i["luongcb"],i["namcongtac"],i["phucap"],i["thunhap"]))
    return
def luufile(path,lstnhanvien):
    f=open(path,"r+",newline="",encoding="utf-8")
    f.seek(0)
    f.truncate(0)
    for i in lstnhanvien:
        h=[]
        for m in i:
            k=[]
            t=[m]
            x=[i[m]]
            k=t+x
            h+=k
        csv.writer(f).writerow(h)
    f.close
    return
def docfile(path,lstnhanvien): 
    f=open(path,encoding="utf-8")
    for i in csv.reader(f):
        dd={}
        x=1
        k=0
        while k<=10:
            lst=[]
            lst+=i
            key=lst[k]
            val=lst[x]
            dd[key]=val
            x+=2
            k+=2
        lstnhanvien.append(dd)
    return 
def maxluong(lstnhanvien):
    h=[]
    for i in lstnhanvien:
        k=[float(i["thunhap"])]
        h=h+k
    d=max(h)
    t=h.index(d)
    print("thông tin nhân viên có lương cao nhất :")
    x=(lstnhanvien[t])
    print('{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format("mã nhân viên","tên nhân viên","lương cơ bản","năm công tác","phụ cấp","thu nhập"))
    print('{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format(x["manv"],x["tennv"],x["luongcb"],x["namcongtac"],x["phucap"],x["thunhap"]))
    return
def xoanhanvien(lstnhanvien):
    h=[]
    xs=str(input("nhập mã nhân viên muốn xóa "))
    for i in lstnhanvien:
        k=[i["manv"]]
        h=h+k
    check=xs in h
    if check==True:
        t=h.index(xs)
        del(lstnhanvien[t])
    else:
        print("mã nhân viên không tồn tại")
    return
def sapxep(lstnhanvien):
    tt=1
    lstmoi=[]
    h=[]
    m=[]
    for i in lstnhanvien:
        k=[float(i["thunhap"])]
        h=h+k
        m=m+k
    h.sort(reverse=True)
    for e in h:
        x=m.index(e)
        moi=(lstnhanvien[x])
        lstmoi.append(moi)
    print("danh sách nhân viên sau khi sắp xếp theo lương")
    print('{:>5}{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format("stt","mã nhân viên","tên nhân viên","lương cơ bản","năm công tác","phụ cấp","thu nhập"))
    for i in lstmoi:
         print('{:>5}{:>20}{:>25}{:>20}{:>18}{:>20}{:>15}'.format(tt,i["manv"],i["tennv"],i["luongcb"],i["namcongtac"],i["phucap"],i["thunhap"]))
         tt+=1
    return
