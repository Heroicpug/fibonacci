#Enter number of terms needed #0,1,2,3,5,8,13,21,34
n=int(input('Enter the no of terms='))
f=0 # intialise first element of series
s=1 # intialise second element of series
if n<=0:
    print('the requested series is',f)
else:
    print(f,s,end='')
for i in range(2,n):
    next=f+s
    print(next,end='')
f=s
s=next
    
