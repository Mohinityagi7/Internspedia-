import random
list = ['Rock','Scissor','Paper']

"""
Rock vs Paper --->  Paper wins
Rock vs Paper --->  Paper wins
Paper vs Scissor --->  Paper wins

"""

while True:
    ccount = 0
    ucount = 0
    uc = int(input("""
    Game Start....
    1 Yes
    2 No | Exit
    
    """))
    if uc == 1:
        for i in range(1,6):
            userInput = int(input("""
            1 Rock
            2 Paper
            3 Scissor
            """)) 

            if userInput == 1:
                uchoice = "Rock"
            elif userInput == 2:
                uchoice = "Paper"
            elif userInput == 3:
                uchoice = "Scissor"
            Cchoice = random.choice(list)
            if Cchoice ==uchoice:
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("Game Draw")
                ucount = ucount+1
                ccount=ccount+1
            elif (uchoice == "Rock" and Cchoice =="Scissor")or(uchoice =="Paper" and Cchoice == "rock")or(uchoice == "Scissor" and Cchoice == "Paper"):
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("You win Game")
                ucount = ucount+1
            else:
                print("Computer Value", Cchoice)
                print("User Value",uchoice)
                print("Computer win Game")
                ccount=ccount+1
       
        if ucount == ccount:
            print("Final Game Draw....")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final You Win The Game....")
            print("User Score",ucount)
            print("Computer Score",ccount)
        else:
            print("Final Computer Win The Game....")
            print("User Score",ucount)
            print("Computer Score",ccount)

    else: 
        break