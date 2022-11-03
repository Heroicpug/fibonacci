s= input ("Enter a string :")
c1=c2=0
for i in s :
    if(i.islower()):
                    c1 = c1 +1
    for u in s:
        if(u.isupper()):
                        c2 = c2+1
if(c1 == 0) :
    print("no lower case character is found in the string :")
else:
    print("total no of lower case character :", c1)
if(c2 == 0) :
    print("no upper case character is found in the string :")
else:
    print("total no of upper case character :", c2)

