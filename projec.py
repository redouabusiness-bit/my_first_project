# اول برنامج ليا في لغة البايتون 

#strin_1 = input("enter first name? \n")
#strin_2 = input("enter age? \n")
#print("hi " + strin_1 + "\n" "your age is: " + strin_2)
#redouan ="34"


#print("welcome in my application \n")
#name = input(" what's your name? \n")
#print("nice to meet you " + name + '\n')
#char_len = len(name)
#print("this is number of latters in your name: " , end="" )
#print(char_len)

#print(len(name))


#first_nume = input("enter name you will use? \n")
#second_nume = input("enter topic of your chanell's? \n")

#print('what about: ' + "(" + second_nume +' with '+ first_nume + ")")


#print(len("octucode"), end= "\n" + "octucode" [3] + '\n')

#cin_card = input("enter the cin num? \n")
#result =  len(str(cin_card))
#print("num of card is: ", end= "" )
#print(result)
#print(type(cin_card))
#print(type(4))

#هذا البرنامج الاول ديالي كيطلب من المستخدم انه يدخل رقمين وكيقوم بجمع الرقمين ويطبع النتيجة للمستخدم 
#لاحقا غادي نقوم بتطويره اكثر 
#num_1 = input("please enter num one \n")
#num_2 = input("please enter num two \n")

#print(int(num_1) + int(num_2))

# هذا هو البرنامج التاني قبل التصحيح الحل الصحيح موجود في الاسطر لي تابعة هذا البرنامج 
#lenght = input("please enter lenght area \n")
#width = input("please enter width area \n ")
#prix = 30 
#result = float(lenght) * float(width)
#print(result * prix)

#length = input("pleas enter the length \n")
#width = input("pleas enter the widgth \n")
#prix = input("pleas enter how mush meter \n")

#proces_1 = float(length) * float(width) 
#proces_2 = proces_1 / prix + '\n'
#trans_variable = str( prix ) #+ str( proces_2 )
#print("sum of length and width is: \n " + proces_1)
#print("amount you must pay is: \n" + proces_2 )

# هذه هو البرنامج التاني ديالي ولي كايحسب مساحة الطول والعرض ديال الغرفة لي بغيت نصبغ
#length = input("enter type of length \n")
#width = input("enter type of width \n")
#prix = input("enter type of how mash for meter \n")

#area = float(length) * float(width) 
#area_1 = float(prix) * area

#str_area = str(area)
#str_area_1 = str(area_1)

#print("total area is: " + str_area)
#print("total for pay is: $" + str_area_1)

#برنامجي الثالث : هو انه يحسب عدد ساعات لي المستخدم كيخدمهم كل اسبوع من خلال عدد الساعات لي كيخدمهم في اليوم 
#str_ours = input(" pleas enter the ours for working in day \n ")

#weeks = int(str_ours) * 7
#minuts = int(str_ours) * 60
#minuts_week = minuts * 6

#print("the number of ours in the week is: " + str(weeks))
#print("the number of minut in the day is:  " + str(minuts))
#print("the number of minut in the week is:  " + str(minuts_week))
#  

#old = int(input("how old are you? \n "))
#print(f"you were born in {2026 - old} and you are {old} years old")

#day_of_week = int(input("enter the day for working in week: \n"))
#hour_of_day = int(input("enter the hours for working in the day: \n"))
#print(f"hours of week is: {day_of_week * hour_of_day } and minutes of week is: {day_of_week * hour_of_day * 60 } and seconds of week is: {day_of_week * hour_of_day * 60 * 60} ")

 
#second = int(input("enter num of second::::: \n"))
#hour = second // 3600
#minute = (second % 3600) // 60
#rameang_second = second % 60
#print(f"the numbers of hours is: {hour} and the numbers of minutes is:  {minute} and the number of secondes is: {second}" )

#برنامج جديد وهو يطلب من المستخدم ادخال كم عمره والتطبيق يشوف اذا المستخدم مسموح له انه يشوف الحوايج لي كايتعرضو في الموقع ولا لا وفقا لعمره 
#age = int(input("welcome to my application: \n" + "enter your age here: \n"))

#if(age < 18):
#    print(f"your age is really small \n")
#else:
#    print(f"welcome to my page \n")


#برنامج جديد يقوم بتحديد هل الرقم الذي ادخله المستخدم سلبي ولا هو رقم ايجابي 
#num = float(input("hi! enter the number here: \n"))
#if num < 0:
#    print("that num is negative \n ")
#elif num == 0:
#    print("that num is 0 \n")
#else :
#    print("that num is positive \n")

#برنامج جديد يطلب من المستخدم انه يدخل الدرجة ديالو في الامتحان ويتحقق اذا كان المستخدم ناجح ولا لا 
#برنامج جديد عن طريقة استخدام LOWER AND UPPER
#area = input("wiche of this is area: \ncasa, rabat, or agadir\n")

#if area.lower() == "casablanca" or area.lower() == "rabat" or area.upper() == "AGADIR":
#    print("your area is on my list ")
#else:
#    print(f"your area is not on my list ")
 #برنامج رقم 6 عبارة عن شروط يجب ان تتحقق من اجل قبول المستخدم في الوظيفة 
#age = int(input("enter your age \n"))
#driver = input('do you have driver lacense \n' + 'enter YES OR NO \n')
#if age >= 18 and driver.lower() == 'yes':
 #   print("you have been accpted for the job \n")
#elif age < 18 :
#    print("you are too young \n")
#elif driver.lower() == 'no' :
#    print("you need a license \n")
#else:
#    print("you did not meet the requirement for working with us \n")
#برنامج رقم 7 عبارة عن الشرووط المتادخلة في بعضها البعض وكفاش نقوكم بتنضميها بالطريقة الصحيحة 
#morocco = input("are you moroccan? \n")
#if morocco == 'yes':
#   print("your answered first questiion \nlet's move second question")
    
#    age = input("are you over 18 years old \n") 
#    if age == 'yes':
#        print("your answered tow \nlet's move third question")
        
#        driver = input("do you have a driver license \n").lower()
#        if driver == 'yes':
#            print("your ready to obtion moroccan citiseship")
#        else:
#            print("your failed the last question \nbut you can try again after you get your driver license")
#    else:
#        print(" sorry! you most over 18 years old to obtain citiseship\ntry again after you have reached")         
            
#else: 
#    print("sorry citiseship is for moroccan only")

print("""
      \U0001f3f4\u200D\u2620\uFE0F
      """)
answered_1 = input("""
                   welcome to my island 
                   choose one of the two doors to enter my world
                    door green 🚪 
                    OR 
                    door red 🚪 
                   """).lower()
if answered_1 == "green":
    print("welcome to the crocodile forest🐊🐊🐊🐊🐊\n")
elif answered_1 == "red":
    box= input("""
          you've entered through the right door, now let the game bigen
          you now have three boxes in front of you! 🚪🚪🚪
          chosse one of the box to descover the surprise that awaits you?
          yellow box📦 
          or
          pink box📦
          or 
          white box📦 
          """).lower()
    if box == "yellow":
        print("welcome to the yellow box \nthis box contains only a lot of spider🕷️🕷️🕷️ ")
    elif box == "pink":
        print("welcome to the pink box \nin the box is your gift: a bouquet of roses🌹🌻🌷🌼 ")
    elif box == "white":
        print("welcome to the box white \nyou chose the right box in your gift is: a box full of money🏦💰💳🪙")
        
        
    else:
        print("your made a typo \nenter the color of one of the boxes in the list🌀💭🤔🔄")
else:
    print("your made a typo \n the door i selected is not on my list🌀💭🤔🔄")   
    
  
    
    



    



    


    




   


    

    






























