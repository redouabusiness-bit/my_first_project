import random
#freinds = input("enter number of friends using comma [,] \n")
#merge = freinds.split(", ")

#if len(merge) < 4 :
#    print("add more than 3 people \n")
#else:
#    num_computer = random.randint(0, len(merge) - 1)
#    print(f"the person who will pay for danner is: {merge[num_computer]}")
    
    
    
    
#freinds = input("enter num of friends \n").split(", ")
#if len(freinds) > 3:
#    print(f"the peson who will pay for danner is: {random.choice(freinds)} \n")
#else:
#print("add more than 3 friends \n ")

#print("Welcom To My Place Rappit \n")
#gred = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
#print(f"{gred[0] }\n{gred[1] }\n{gred[2] }\n")
#place_rappit = input(f"where is should the rappit 🐰 go \nplease, enter the row and column with places: .....")
#if len(place_rappit) != 2:
#    print(f"sorry, the {place_rappit} is not correct \n")
#else:  
#    row = int(place_rappit[0]) - 1
#    column = int(place_rappit[1]) -1
#    gred[row][column] = "🐰"
#    print(f"{gred[0] }\n{gred[1] }\n{gred[2] }\n")

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
choose_user = input("Enter yoyu choose (rock, paper, scissors): \n").lower()
images_game =[]
   
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
images_game = {"rock": rock, "paper": paper, "scissors": scissors}
choices = ["rock", "paper", "scissors"]
num_computer = random.choice(choices)
result = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    
    
   
  
    
if choose_user not in result:
        print("sorry, the input is incrrect \n")
elif choose_user == num_computer:
       print(f"you choise is: {images_game[choose_user]} \ncomputer choose is: {images_game[num_computer]} \n") 
       print(" the result is drew! \n")
elif result[choose_user] == num_computer:
        print(f"you choise is: {images_game[choose_user]} \ncomputer choose is: {images_game[num_computer]} \n")
        print("you won! \n")
elif result[choose_user] != num_computer:
        print(f"you choise is: {images_game[choose_user]} \ncomputer choose is: {images_game[num_computer]} \n")
        print("computer won! \n")
else:
        print("sorry, the input is incorrect \ntry again \n") 



        
  
  
   


   
    
   

    
    
    






    




#print(f"Success ", *gred, sep="\n")


#هنا قسمت السطر بوحدو والمكان بوحدو لان اليوزر دخلهم لجوج معا بعضيتهم 

    






    


    



















    

    

    