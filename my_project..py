import random
print("hi evryone, welcome to my game! \n")
print("""
      which method do you prefer for the programme? \n
      1 method random.random()\n
      2 method random.randint()\n
""")
choose = int(input("please, enter the one of two method | \n1 \nor \n2 \n"))

if choose == 1:
    proces_1 = random.random()
    if proces_1 >= 0.5:
        result = 'king'
    else:
        result = 'write'
elif choose == 2:
    proces_2 = random.randint(0, 1)
    if proces_2 == 0:
        result = 'king'
    else:
        result = 'write'       
else:
    print(f"sorry, {choose} is not equal 1 or 2 \n")
    exit()
    
    


    
user_ask = input("pleas, enter one of two option \nking or write \n").lower()
if user_ask == result:
    print("you won! \n")
    print(f"your computer input is: {result}")
else:
    print(f"sorry, input for you doesn't selected for computer selected\n")
    print(f"your computer input is: {result}")
     
    

    
    




    
    

    





    
    
    


    
    
 
    
    
  


    


    
    

    

    
    
