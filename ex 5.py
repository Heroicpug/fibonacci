def fact (n):
    if n == 1 :
        return n
    elif n>1:
        return n*fact(n-1)
n = int(input("Enter the number  :"))
print("factoril of",n,"=",fact(n))
