principal_amount=250000
annual_rate= 0.05
years= 30
r=annual_rate/12
n=years*12
M = principal_amount*(r*(1+r)**n) / ((1+r)**n - 1)
print(M)