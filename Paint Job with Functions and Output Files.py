import math
#this function keeps asking the user for a number 
def getFloatInput(message):
    number = -10
    while number < 0:
        try:
            number = float(input(message))
            return number
        except:
            print("Error: enter a number")



#this function calculate how many gallons we need
def getGallonsOfPaint(sqfeet, pergallon):
     #math.ceil will round up
    gallon= math.ceil(sqfeet/pergallon)
    return gallon 
    


#this function calculate how many houre we need
def getLaborHours(pergallon,totalgallons):
    total= pergallon*totalgallons
    return total


#this function calculate the labor cost
def getLaborCost (pergallon, perhour):
    cost=pergallon*perhour
    return cost


#this function calculate the cost of the paint
def getPaintCost  (gallons, price):
    cost= gallons*price
    return cost



#this function calculate the tax rate
def getSalesTax(State): 
    


    if State == "CT": 
        return 0.06
    elif State == "MA": 
        return 0.0625
    elif State == "ME": 
        return 0.085
    elif State == "NH": 
        return 0.0
    elif State == "RI":
        return 0.07
    elif State == "VT":
        return 0.06
    else:
        return 0.0




#this function does calculation and prints to the screen and prints to the file

def showCostEstimate(WallSpace,PaintPrice, FeetPerGallon, Hours, LaborCharge, state,name):
    file= open(name+"_PaintJobOutput.txt","w")
    gallonsNeded = getGallonsOfPaint (WallSpace,FeetPerGallon)
    print ("Gallons of paint: ",gallonsNeded)
    file.write("Gallons of paint: "+str (gallonsNeded)+"\n")


    
    LaborHours = getLaborHours(Hours,gallonsNeded)
    print ("Hours of labor:" ,LaborHours)
    file.write("Hours of labor:" +str (LaborHours)+"\n")



    
    paintcharge = getPaintCost ( gallonsNeded,PaintPrice)
    print ("paint charges: $" +str (paintcharge))
    file.write("paint charges: $" +str (paintcharge)+"\n")





    Cost= getLaborCost (LaborHours, LaborCharge)
    print ("Labor charges: $"+str (Cost))
    file.write("Labor charges: $"+str (Cost)+"\n")




    BeforeTax= paintcharge+Cost
    taxRate=getSalesTax(state)
    tax= taxRate*BeforeTax
    taxf=format(taxRate*BeforeTax,".2f") 
    print ("tax: $"+str(taxf ))
    file.write("tax: $"+str(taxf )+"\n")
    


    Total=format(BeforeTax+tax,".2f") 
    print ("Total Cost: $"+str(Total))
    file.write("Total Cost: $"+str(Total)+"\n")



    
    file.close()

def main():
    WallSpace = getFloatInput ("enter wall space in square feet: ")
    PaintPrice = getFloatInput ("enter paint price per gallon: ")
    FeetPerGallon = getFloatInput ("enter feet per gallon: ")
    Hours = getFloatInput ("how many labor hours per gallon: ")
    LaborCharge = getFloatInput ("labor charge per hour: ")

    state =input("state job is in: ")
    name = input ("customer last name: ")
    showCostEstimate(WallSpace,PaintPrice, FeetPerGallon, Hours, LaborCharge, state,name)
main()
