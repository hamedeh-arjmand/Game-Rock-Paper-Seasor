import random

print("rock...")
print("paper...")
print('seasor...')
print('')
player1= input("plyer1:please guess: ").lower()
randomNum = random.randint(1,3)

if randomNum == 1:
    player2 = "rock"
elif randomNum == 2:
    player2 = "paper"
elif randomNum == 3:
    player2 = "seasor"

print("Player2 =",player2)

if player1 == player2:
    print("try again,nobody win!")

elif player1 == "rock" and player2 == "paper":
    print("*player2,win*")
elif player1 =="rock" and player2 == "seasor":
    print("*player1,win*!")

elif player1 == "paper" and player2 == "rock":
    print("*player1,win*")
elif player1 == "paper" and player2 == "seasor":
    print("*player2,win*")

elif player1 == "seasor" and player2 == "paper": 
    print("*player1,win*")
elif player1 == "seasor" and player2 == "rock":
    print("*player2,win*")

else:
    print("some answer is wrong!")