#Insert letter in parenthesis
Unknown_data=input("What do you need: position(x),velocity(v),acceleration(a)")
#We ask all the variables except the one we want to know,then we operate the ecuation with the variable cleared
if Unknown_data== "x":
    initial_position=float(input("Insert initial position"))
    initial_velocity=float(input("Insert velocity"))
    acceleration=float(input("Insert acceleration"))
    time=float(input("Insert time"))
    position=(initial_position + initial_velocity*time + 0.5*acceleration*time**2)
    print(position)
if Unknown_data== "v":
    initial_velocity=float(input("Insert velocity"))
    acceleration=float(input("Insert acceleration"))
    time=float(input("Insert time"))
    velocity=(initial_velocity + acceleration * time)
    print(velocity)
if Unknown_data== "a":
    initial_position=float(input("Insert initial position"))
    initial_velocity=float(input("Insert velocity"))
    time=float(input("Insert time"))
    position=float(input("position"))
    velocity=float(input("Insert velocity"))
    acceleration=(velocity**2 - initial_velocity**2)/(2*(position-initial_position))
    print(position)

