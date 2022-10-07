def reverse(str1):
    if(len(str1)==0):
       return str1
    else:
        return reverse(str1[1:])+str1[0]
string=input('please enter your own string :')
str1 = reverse(string)
print('string in reverse order:',str1)
if(string==str1):
   print('this is a palindrome')
else:
    print('this is not a palindrome')
