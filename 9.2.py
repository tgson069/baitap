can=["canh","tan","nham","quy","giap","at","binh","dinh","mau","ky"]
chi=["than","dau","tuat","hoi","ty","suu","dan","mao","thin","ty","ngo","mui"]
a=int(input("nhap nam "))
def tinhnamam(a):
     m=a%10
     h=a%12
     x=can[int(m)]
     y=chi[int(h)]
     print(x,y)
tinhnamam(a)
