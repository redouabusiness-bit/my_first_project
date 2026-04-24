
import random
print("Welcome To The Rock, Paper, Scissors Game? \n")
confirm = input(f"Press Enter To Continue Or Type (Help) For The Rules \n").lower()
if confirm == "help":
    print("""
          ******* RULES ******* \n
          1) You choose and the computer chooses \n
          2) Rock smashes scissors -> rock wins \n
          3) Scissors cut paper -> scisseors wins \n
          4) Paper covers rock -> paper wins
          """)
   
rock =  """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    
    """
paper =  """
_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors =  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
choose_user = input("Enter yoyu choose (rock, paper, scissors): \n").lower()
if choose_user not in ["rock", "paper", "scissors"]:
    print("sorry, the input for you is incorrect \n")
    exit()
else: 
     if choose_user == "rock":
        print(f"you choise is: {rock} \n")
     elif choose_user == "paper":
        print(f"you choise is: {paper}")
     else:
        print(f"you choise is: {scissors}")
        
num_computer = random.choice(["rock", "paper", "scissors"])
if num_computer == "rock":
              print(f"computer choise is: {rock}")
elif num_computer == "paper":
              print(f"computer choise is: {paper}")
else:
              print(f"computer choise is: {scissors}")
if choose_user == num_computer:
                print(f"the result is drew! \n")
elif (
                choose_user == "rock" and num_computer == "scissors"
                or
                choose_user == "paper" and num_computer == "rock"
                or
                choose_user == "scissors" and num_computer == "paper"  
            ):
                print(f"you won! {choose_user} defeat {num_computer} \n")
else:
                print(f"computer won! {num_computer} defeat {choose_user} \n")
                
            
        
        
        

    
    
   
  
 