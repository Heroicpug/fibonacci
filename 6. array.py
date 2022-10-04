even=0
odd=0
numberlist=[] # empty list
size=int(input('Enter the total number of list element:'))
for i in range(size):
    element=int(input('please enter the value of % d element:'%i))
    numberlist.append(element)
print('find odd and even here')
for i in range(size):
    if(numberlist[i]%2)==0:
        print(numberlist[i],'is even')
        even=even+1
print('no of even number:',even)
print('no of odd number:',odd)      
