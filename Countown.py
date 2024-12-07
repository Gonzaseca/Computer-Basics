number=10
wires=['green','red','yellow','blue']
while number>0:
    print(number)
    cut=input(f"Cut one {wires}" )
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
    else:
        if number> 1:
            print("Are you going to cut or not?")
        else:
            print("You could at least try")
    number-= 1
else:
    print("¡BOOM!")