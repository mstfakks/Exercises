import random
x1=0
x2=0
x3=7
y1=0
y2=5
y3=0

degerler=range(40)
liste1=random.sample(degerler,10)
liste2=random.sample(degerler,10)
liste3=[(liste1[0],liste2[0]),(liste1[1],liste2[1]),(liste1[2],liste2[2]),(liste1[3],liste2[3]),(liste1[4],liste2[4]),(liste1[5],liste2[5]),(liste1[6],liste2[6]),(liste1[7],liste2[7]),(liste1[8],liste2[8]),(liste1[9],liste2[9])]

#üçgen = (0,0),(0,5),(7,0)

def alan(x1,y1,x2,y2,x3,y3):
    return abs ((x1*(y2-y3)+x3*(y1-y2)+x2*(y3-y1))/2)
for a,b in liste3:
    Area=alan(x1,y1,x2,y2,x3,y3)
    area1=alan(a,b,x2,y2,x3,y3)
    area2=alan(x1,y1,a,b,x3,y3)
    area3=alan(x1,y1,x2,y2,a,b)

    if(area1+area2+area3==Area):
        print("True")
    else:
        print("False")
    