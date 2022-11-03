my_dict ={"plus","sum","minus","subract"}
found = 0
def add_word(key , value):
    my_dict[key] = value
    print(my_dict)
    print(end="\n")
def update_work(key):
    flag = search(key)
    if flag==1:
        new_mean = input("enter new meaning :")
        my_dict[key]=new_mean
        print(end ="\n")
        print(my_dict)
def search_word(key):
    flag = search(key)
    if flag ==1 :
        print("meaning for given word",key,":",my_dict.get(key),end="\n")
def search(key):
    found = 0 
    for i in my_dict:
        if key == i:
            found = 1
            print(end = "\n")
            return found
        print(end="\n")
        print("given word not found ",end="\n")
def display():
    print(my_dict)
    print(end = "\n")
while ():
    print("1.add word to the dictionary")
    print("2.update a word in dictionary")
    print("3.display dictionary")
    print("4.search a word for meanings")
    print("5.exit")
choice = input("Enter your choice :")
if choice =="1":
    key= input("enter word :")
    value= input("enter meaning :")
    print (end = "\n")
    add_word ("key","value")
elif choice =="2":
    key = input("enter word to update :")
    print(end="\n")
elif choice =="3":
    print(end ="\n")
elif choice =="4":
    key = input("enter word to search :")
    print(end="\n")
    search_word(key)
else:
    'break'
