# while loop test
#i = 0
#while(i < 10):
#    print(i)
#    i = i + 1
# This is a comment
from math import pi

#I will use this space to run a program for thermal engineering to make my life easier 

# The project is to make a 4 cylinder car engine to make as much power as possible

bore = 0
stroke = 0
L = 0 # stroke of the piston
A = 0 # area of the piston
pd = L*A # piston displacement
n = 0 # number of revolutions
W_i = 0 # indicated work
W_f = 0 # friction work

# Not sure if W_i and W_f are usually given or not

W = 0 # theoretical work
W_b = W_i - W_f # brake work

brakeEfficiency = W_b / W # brake efficiency
# might need to use brake efficiency to find W_b

p_mb = W_b / pd # brake mean effective pressure
bhp = (p_mb*L*A*n)/33000 # brake horsepower using mean effective pressure