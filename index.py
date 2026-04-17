
print("Welcome To My Application \n")
books = []
books_for_user_in_buying = []

user_book = input("enter one of the book you own \n")
#هنا طلبت من المستخدم انه يدخل احد الكتب لي كايمتلكها في الوقت الحالي وحفظتها في متغير
books.append(user_book)
#هنا خديت المتغير لي ديجا قمت بانشائه ودرت ليه تحديث وخزنت في الكتاب لي المستخدم ادخله
user_book = input("do you have any more books, if you don't have it, you can skip it, \nif you have another book, please add it here. or skip it \n").lower()
#هنا طلبت من المستخدم انه يدخل كتاب اخر الى كان عندو
#لكن في حالة الى ماعندوش يدير سكيب ويدوز للسؤال التالي 
#وهنا خاصني نشوف واش المستخدم دار سكيب ولا كمل ودخل كتاب اخر 

#في الحالة انه الى دار سكيب نطبع ليه القايمة دبال الكتب لي كايمتلكها وننتقل مباشرة الى السؤال التالي 
#وفي حالة الى دخل كتاب جديد ندير تحديث لقائمة الكتب وبرضو نطبعها ليه وننتقل الى السئؤال التالي
#

if user_book:
    #هن قمت بالمقارنة واش المدخل ديال المستخدم خاوي ولا لا
    #في حالة ما كنش خاوي هاشنو خاصك دير 
    books.append(user_book)
    #غادي ياخد التطبيق داك الكتاب الثاني لي المستخدم قام بادخاله وغادي يزيدو مع الكتاب السابق
    print(f"This is a list of the books you currently own. {books} \n")
    #هنا التطبيق غادي يقوم بطباعة قائمة الكتب لي المستخدم كايمتلكها 
    dream_books = input("Is there a book you dream of owning someday? \nIf there's no way to skip \n").lower()
    #هنا التطبيق غادي يتحول للسؤال التالي وغادي يسول المستخدم واش كاين شي كتاب كاتحلم انك تمتلكو شي نهار وغادي يخزن المدخل ديال المستخدم في المتغير هذا
    #وخاص التطبيق هنا يتاكد بان المستخدم دخل مدخل ومادرش سكيب عن طريق المقارنة

    
    if dream_books:
         #هنا غادي نعود نشوف واش المستخدم دخل كتاب اخر ولا دار سكيب 
         #في حالة دخل كتاب اخر ههي الخطوات لي غادي يدير التطبيق 
       
         #غادي ننشأ متغير باش نخون فيه الكتب لي كايحلم المستخدم انه يمتلكهم ونخليه خاوي حاليا 
    
        books_for_user_in_buying.append(dream_books)   
         #هنا قمت بتحديث المتغير وضفت ليه القيمة لي المستخدم ادخلها اخر مرة 
    
        
        dream_books = input("Is there any other book you dream of owning? If not, skip this. \n").lower() 
         #هنا غادي نسول المستخدم واش كاين شي كتاب اخر كاتحلم انك تمتلكه في حالة ماكانش يدير سكيب 
   
   
        if dream_books:
            books_for_user_in_buying.append (dream_books)
            #هنا غادي نشوف واش المستخدم دار سكيب ولا اضاف كتاب اخر يحلم بامتلاكه 
            #هنا جبت المتغير لي فيه الكتب لي المستخدم كايحلم انه يمتلكها وضفت عليهاالكتاب لي اضافه في الاخير 
            print(f"The list of books you dream of buying in the future includes {books_for_user_in_buying} \n")
            #هنا قمت بطباعة للمستخدم التحديث الجديد لقائمة الكتب التي يحلم بامتلاكها
            apdate_dream_books = input("Is there any book from your dream book list that you've actually bought? Or if you haven't bought any yet, skip it. \n").lower()
            #هنا سولت المستخدم واش كاين شي كتاب من قائمة الكتب التي يحللم بمتلاكها بالفعل هو شراه او متلكو وفي حالة الى ماكانش يدير سكيب
            if apdate_dream_books in books_for_user_in_buying:
                #هنا تاكدت واش المستخدم دخل قيمة ولا دار سكيب 
                books.append(apdate_dream_books)
                #هنا انا خديت المكتبة ديال المستخدم وضفت ليها داك الكتاب لي شراء المستخدم دبا خاصني نحيدو من قائمة ديال التمني 
                books_for_user_in_buying.remove(apdate_dream_books)
                #هنا انا عاودت درت تحديث لقائمة التمني وحيدت منها الكتاب لي المستخدم شراه 
                print(f"These are the books you have after the update: {books} \n")
                print(f"This is the list of books you will buy in the future after the latest update. {books_for_user_in_buying} \n")
    
                #هنا قمت بكباعة للمستخدم التحديث الجديد ديال قائمة الكتب لي بالفعل هو كايمتلكها 
                #print(f"This is the list of books you dream of owning after the update. {books_for_user_in_buying} \n")
                #هنا طبعت للمستخدم قائمة الكتب لي كايحلم انه يشريها من بعد ماخديت منها الكتاب لي هو شراه سابقا اي من بعد التحديث
                apdate_books = input("Did you give away any books from your library to someone? Or skip this if you didn't. \n").lower()
                #هنا سولت المستخدم واش كاين شي كتاب من المتبة ديالو عطاه لشي واحد او مابقاش عندو 
                #الى كانت عندو القائمة ممشاش منها حتى كتاب قلت ليه دير سكيب 
                if apdate_books in books:
                    #هنا تاكدت بان المستخدم ما دارش سكيب 
                    books.remove(apdate_books)
                    #هنا من بعد ماتاكدت هويت المكتبة ديال المستخدم ومسحت منها الكتاب لي مابقاش فيها يعني لي المستخدم لاحو او عطاه لشي واحد 
                    print(f"This is the update to your library after I gifted one of the books in it. {books} \n")
                    #هنا قمت بطباعة المكتبة للمستخدم من بعد ما مسحت منها الكتاب لي عطاه لشي واحد 
                else:
                    print(f"Also, since you haven't donated any books from your library yet, these are the books that remain after the update. {books} \n")
            else:
                print(f"Okay, since you haven't bought any books from your wish list yet, here's the updated list. {books_for_user_in_buying} \n")
        else:
            print(f"Okay, you only have one book that you dream of buying in the future, and it is: {books_for_user_in_buying} \nand This is your personal library: {books}")
    else:
        print(f"Excellent, so this is your personal library. {books} \n")
        loop = input(f"Have you donated any of the books from your library? \n skippppp \n")
        books.remove(loop)
        print(f"This is your library after you donated one of the books. {books} \n")
else:
    print(f"This is your list of books: {books} \n")
    dream_books = input("Is there a book you dream of owning someday? \nIf there's no way to skip \n").lower()
    print(f"this is your library dream: {dream_books}")

    
    
    
        
        
    
    
    













     

        
        
        
    
    
    

