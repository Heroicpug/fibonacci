def returnsum(mydict):
    s=0
    for i in mydict:
        s = s+ mydict[i]
        return s
dictl ={'a':100,'b':200,'c':300}
print("dictionaries contain=",dictl)
print("sum :",returnsum(dictl))

