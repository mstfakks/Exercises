sayi=int(input("Bir sayı giriniz: "))
bolen=[]
for a in range(1,sayi+1):
    if (sayi%a==0):
        bolen.append(a)
    else:
        pass
print(sayi,"sayısının tam bölenleri:\n",bolen)
    
