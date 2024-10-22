name=input("Hi,what's your name?")
#Checks if the name is made justby letters
if name.isalpha():
    print("Hi",name,"nice to meet you")
    #Asks the date of birth(dob) and the decomposes it on a list so we are able to check the values
    dob=input("When where you born?")
    birthday_data=dob.split("/")
    if len(birthday_data)==3:
        age=2024 - int(birthday_data[2])
        print("So yo are",age, "years")
        #Asks hobbies in a certain format to avoid errors
        hobbies=input("Tell me 2 of you hobbies")
        hobbies_list=hobbies.split(",")
        if len(hobbies_list)==2:
            print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue enjoying with",hobbies_list[0],"and",hobbies_list[1])
        while len(hobbies_list)!=2:
            hobbies=input("Please write just 2 of your hobbies separated by commas")
            hobbies_list=hobbies.split(",")
            if len(hobbies_list)==2:
                print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue with",hobbies_list[0],"and",hobbies_list[1])
    while len(birthday_data)!=3:
        dob=input("Use format DD/MM/YYYY")
        birthday_data=dob.split("/")
        if len(birthday_data)==3:
            age=2024 - int(birthday_data[2])
            print("So yo are",age, "years")
            #Asks hobbies in a certain format to avoid errors
            hobbies=input("Tell me 2 of you hobbies")
            hobbies_list=hobbies.split(",")
            if len(hobbies_list)==2:
                print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue enjoying with",hobbies_list[0],"and",hobbies_list[1])
            while len(hobbies_list)!=2:
                hobbies=input("Please write just 2 of your hobbies separated by commas")
                hobbies_list=hobbies.split(",")
                if len(hobbies_list)==2:
                    print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue with",hobbies_list[0],"and",hobbies_list[1])
#Repeats this until an accepted value is given
else:
    while name.isalpha()==False:
        name=input("Enter a valid name")
        if name.isalpha():
            print("Hi",name,"nice to meet you")
            #Asks the date of birth(dob) and the decomposes it on a list so we are able to check the values
            dob=input("When where you born?")
            birthday_data=dob.split("/")
            if len(birthday_data)==3:
                age=2024 - int(birthday_data[2])
                print("So yo are",age, "years")
                #Asks hobbies in a certain format to avoid errors
                hobbies=input("Tell me 2 of you hobbies")
                hobbies_list=hobbies.split(",")
                if len(hobbies_list)==2:
                    print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue enjoying with",hobbies_list[0],"and",hobbies_list[1])
                while len(hobbies_list)!=2:
                    hobbies=input("Please write just 2 of your hobbies separated by commas")
                    hobbies_list=hobbies.split(",")
                    if len(hobbies_list)==2:
                        print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue with",hobbies_list[0],"and",hobbies_list[1])
            while len(birthday_data)!=3:
                dob=input("Use format DD/MM/YYYY")
                birthday_data=dob.split("/")
                if len(birthday_data)==3:
                    age=2024 - int(birthday_data[2])
                    print("So yo are",age, "years")
                    #Asks hobbies in a certain format to avoid errors
                    hobbies=input("Tell me 2 of you hobbies")
                    hobbies_list=hobbies.split(",")
                    if len(hobbies_list)==2:
                        print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue enjoying with",hobbies_list[0],"and",hobbies_list[1])
                    while len(hobbies_list)!=2:
                        hobbies=input("Please write just 2 of your hobbies separated by commas")
                        hobbies_list=hobbies.split(",")
                        if len(hobbies_list)==2:
                            print("Bye",name,"I will call you",dob,"for your birthday","I hope you continue with",hobbies_list[0],"and",hobbies_list[1])


