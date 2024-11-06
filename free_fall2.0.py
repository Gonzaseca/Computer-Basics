#We ask for the gravity and the initial height
g=(float(input("Insert gravity")))
y0=(float(input("Insert initial height")))
#Initial velocity is always 0
v0=0
#We ask for the maximum value time has in the interval
maximum_time=int(input("Insert maximum time of the interval"))
elements_interval=int(input("Insert the number of elements of the interval"))
#We create a list to store the value of the positions and another one for the times
positions=[]
times=[]
import numpy as np
final_times=np.linspace(0,maximum_time,elements_interval)
y=y0 + v0 - 0.5*g*final_times**2
y=np.where(y<0,0,y)
print(y)
diff=np.diff(-y)
print(diff)
mean=np.mean(diff)
print(mean)