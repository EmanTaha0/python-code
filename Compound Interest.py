#compound interest assignment 

PV = float(input("enter the starting principal: " ))
R = float (input("enter the annual interest: " ))
#r is the rate converted to a decimal from percent 
r = R/100
M = int (input("how many times per year is the interest compounded? "))
T = int (input("for how many years will the account earn interest? "))
FV = PV*((1+r/M)**(M*T))
# format    FV to have 2 numbers after the decimal 
A = format (FV, ".2f")
print ("at the end of ",T ,"years you will have $" , A)

