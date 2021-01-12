with open("C:/Users/PC/numere.txt",'r') as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    print(b)
if int(a)<int(b):
    print(a)
with open('c:/Users/PC/minim.txt','w') as f:   
    f.write(str(a))or(str(b))
    
