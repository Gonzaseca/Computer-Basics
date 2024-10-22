#We ask for the gravity and the initial height
g=(float(input("Insert gravity")))
y0=(float(input("Insert initial height")))
#Initial velocity is always 0
v0=0
#We ask for the maximum value time has in the interval
maximum_time=int(input("Insert maximum time of the interval"))
#We create a list to store the value of the positions and another one for the times
positions=[]
times=[]
#We use a loop to create the values of the interval
for t in range(0,maximum_time+1,):
    #Free fall equation
    y=y0 + v0 - 0.5*g*t**2
    #As the position cannot be under 0 we force the loop to make all values after 0
    if y<=0:
        y=0
    #We add each value to their list
    positions.append(y)
    times.append(t)
#We print both lists
print(times)
print(positions)