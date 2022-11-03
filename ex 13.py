n = int(input("enter the number of disks :"))
a=[]
b=[]
c=[]
for k in range (n):
    a.append(n-k)
    print("k value =",k)
    print("n-k value =",n-k)
print(a,b,c)
def tower2(n,frma , toc, auxb):
    if n == 1:
        toc.append(frma .pop())
        print(a,b,c)
        return 
    tower2(n-1,  frma ,auxb , toc)
    toc.append (frma .pop())
    print(a,b,c)
    tower2(n-1,auxb ,toc,frma)
tower2(n,a,c,b)
