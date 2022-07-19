import random
def rolldice(min,max):
    while True:
        print("Rolling dice......")
        number = random.randint(min,max)
        print(f"Your number : {number}")
        choice = input("Do you want to Roll The Dice again? (y/n)")
        if choice.lower() == 'n':
            break
rolldice(1,6)