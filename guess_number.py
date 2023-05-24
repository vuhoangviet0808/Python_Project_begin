import random

random_number = random.randint(1,100)

guess = int(input("Enter your guess number:"))

count = 1

while(random_number != guess):
    count+=1
    if(count>6):
        print("You lose")
        break
    if(random_number<guess):
        print("Your number is higher than\n")
        guess = int(input("Enter your difference number:"))
    else:
        print("Your number is lower than\n")
        guess = int(input("Enter your difference number:"))


if(random_number==guess):
    print("You win.You guessed it right!! ")
