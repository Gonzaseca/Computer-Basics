#Initial number
number=10
#Different wires
wires=['green','red','yellow','blue']
#This loop allows us to ask the user every "second" 
while number>0:
    print(number)
    #This variable stores the wires the user wants to cut
    cut=input(f"Cut one {wires}" )
    #Using the elements of the list I can differentiate the wires and give different responses to the being cut
    if cut== wires[0]:
        print("Well done")
        break
    if cut== wires[1]:
        print("¡BOOM!")
        break
    if cut== wires[2]:
        number-= 1
        continue
    if cut== "blue":
        number-= 1
        continue
    #In case the user doesn't enter a valid input or skips the question this message appears
    else:
        if number> 1:
            print("Are you going to cut or not?")
        #This messages appears if the last input is invalid
        else:
            print("You could at least try")
    #This is what makes the countdown work
    number-= 1
#Final explosion
else:
    print("¡BOOM!")