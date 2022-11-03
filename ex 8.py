string = input("Enter your own string :")
strl =""
for i in string:
    strl = i + strl
print("string in reverse order:",strl)
if(string == strl):
    print("this is a palindrome string")
else:
     print(" this is not a palindrome string")

