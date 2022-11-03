m = int(input("Enter the maximun Value :"))
eventotal = 0
oddtotal = 0
for number in range(1,m+1):
    if(number %2==0):
              eventotal +=1
    else:
         oddtotal +=1
    print("total number of even number from 1 to",m,"eventotal")
    print("total number of odd number from 1 to",m,'oddtotal')
