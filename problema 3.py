#a-albe, x-alebastre,y-rosii, s-suma
with open("C:/Users/PC/globulet.txt",'r') as f:
    a=f.readline()
    y=int(a)*3
    x=int(a)+int(y)-2
    s=int(a)+int(x)+int(y)
with open ('c:/Users/PC/bradut.txt','w') as f:
    f.write(str(s))