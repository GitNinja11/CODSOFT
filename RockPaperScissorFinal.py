#RockPaperScissor
import random

def match():
    choice=["rock","paper","scissor"]

    #computer's Choice
    g=random.randint(0,2)
    computer=choice[g]

    #User's choice
    while True:
       try:
          n=int(input("Enter you choice (0:rock , 1:paper, 2:scissor)"))
          if n in [0,1,2]:
            user=choice[n]
            break
          else:
              raise ValueError("Invalid Input.Please enter (0:rock , 1:paper, 2:scissor): ")
       except ValueError as e:
            print("Invalid Input.Please enter (0:rock , 1:paper, 2:scissor): ")
    #Match
    if user==computer:
        print(f"It's a tie! Your choice: {user}, Computer's choice: {computer}")
        return "tie"
    elif (user=="rock" and computer=="scissor") or (user=="scissor" and computer=="paper") or (user=="paper" and computer=="rock") :
        print(f"You win! Your choice: {user}, Computer's choice: {computer}")
        return "user"
    else:
        print(f"You Loose! Your choice: {user}, Computer's choice: {computer}")
        return "computer"
                        

def play():
    user_score,computer_score=0,0
    print("Welcome to Rock Paper Scissor Game😊")
    print("The Rules for the Game are:")
    print("0:Rock")
    print("1:Paper")
    print("2:Scissor")
    while True:
        try:
            want=int(input("To start the game press 1, To Exit press 0 : "))
            if want==1:  
               result=match() 
               if result=="user":
                  user_score+=1
               elif result=="computer":
                  computer_score+=1
               print(f"Scores: You {user_score} - {computer_score} Computer")   
            try:
                play_again= int(input("Enter 2 to play again and 0 to exit"))
                if play_again==0:
                    print("Exit")
                    break
                elif play_again==2:
                    True
                else:
                    print("Invalid input. Please enter a valid number.") 
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
                print("Invalid input. Please enter a valid number.")                       
    else:
        print("Exit")
       

play()


           