import time
name = input("what is ur name ?")
print("Hi"+ name,"start the game")
print(" ")
time.sleep(0)
print("start ur guess")
time.sleep(0.5)
word ="secret"
guesses = ""
turn = 10
while turn >0:
    failed = 0
    for char in word :
        if char in guesses : 
            print (char)
        else :
            print("_")
            failed = failed +1
        if failed == 0 :
            print("u won")
            break
            print("")
        guess = input("guess a character:")
        guesses += guess
        if guess not in word :
            turn -=1
            print("wrong")
            print("u have", +turn,"more guesses")
        if turn == 0:
            print("u lose")
