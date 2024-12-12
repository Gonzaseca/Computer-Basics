import numpy as np
list=[]
for i in range(1,11):
    x=list.append(np.random.randint(10,50+1))
print(list)
average=np.mean(list)
overaverage=0
for i in range(len(list)):
    if list[i]>average:
        overaverage+=1
std=np.std(list)
print(f"Our marks are {list} , the average score is {average}, the standard deviation of our marks is {std} ,there are {overaverage} values over the average score")