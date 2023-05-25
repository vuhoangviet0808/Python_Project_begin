import random

def lose():
    c = input("You want play again? (Yes/No):")
    c = c.title()
    if(c == 'Y' or c == 'y' or c == 'Yes'):
        return 'Yes'
    if(c == 'N' or c== 'No'):
        return 'No'


com = ["Rock","Paper","Scissors"]
def game():
    print("1:Rock")
    print("2:Paper")
    print("3:Scissors")

    global b
    b = int(input("Nhap vao so cua ban:"))


    a = random.choice(com)

    if(a == com[b-1]):
        print("Draw!!")
        b = lose()
        if (b == 'Yes'):
            return game()
        if b == 'No':
            return 0

    if (a != com[b-1]):
        if(a == 'Rock'):
            if b == 3:
                print("You win.Great!!")
                c = lose()
                if c == 'Yes':
                    return game()
                if c == 'No':
                    return 0

            if b ==2:
                print("You lose")
                c = lose()
                if c == 'Yes':
                    return game()
                if c == 'No':
                    return 0
        elif a == 'Paper':
            if b == 1:
                print("You win.Great!!")
                c = lose()
                if c == 'Yes':
                    return game()
                if c == 'No':
                    return 0
            else:
                print("You lose")
                c = lose()
                if c == 'Yes':
                    return game()
                else:
                    return 0

        else:
            if b == 2:
                print("You win.Great!!")
                c = lose()
                if c == 'Yes':
                    return game()
                if c == 'No':
                    return 0
            else:
                print("You lose")
                c = lose()
                if c == 'Yes':
                    return game()
                else:
                    return 0

game()





