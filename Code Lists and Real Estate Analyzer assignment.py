'''
#1 getFloatInput takes a message to print to the user asking for a number.
If the user enters a number smaller than 0 or enters something that is
not a number, keep asking for a good positive number.
'''
def getFloatInput(message):
    number = -10
    while number <= 0:
        try:
            number = float(input(message))
            if number > 0:
                return number
        except:
            print("Input a number that is greater than 0.")


'''
#2 getMedian takes a list and returns the median (number in the middle).
- If the number of entries in the list is odd, divide the count by 2,
 and use that entry as the median
- If the number of entries in the list is even divide the count by 2.
Take that entry and the entry before it and average the two elements
and use that as the median.
'''
import math

# [1, 5, 7, 9, 10]   5/2 -> 2.5 -> math.ceil(2.5) -> 3
# [1, 5, 7, 9]  4/2 -> 2.0  At 1
#  0  1  2  3
def getMedian(myList):
    count = len(myList)
    if count % 2 == 1:   # odd
        return myList[math.ceil(count/2)]
    else:
        middle = int(count/2)
        num = myList[middle]
        before = myList[middle  - 1 ]
        return (num + before)/2

'''
#3 main
'''

def main():
   
    # create an empty list
    pricesList = []
   
    # a loop that repeats until the user enters a N to exit the loop.
    price = getFloatInput('Enter property sales value: ')
    again = input('Enter another value Y or N: ')
    pricesList.append(price)
    # change again to be upper case only
    # if again is NOT equal (!=)
    while again.upper() != 'N':
        if again.upper() == 'Y':
            price = getFloatInput('Enter property sales value: ')
            # add the number to the list
            pricesList.append(price)
           
        again = input('Enter another value Y or N: ')

   
    # sort the list
    pricesList.sort()
   
    # print the sorted list
    num = 1
    for e in pricesList:
        print("Property", num, "$",  format(e, ",.2f")  )
        num = num + 1
   
    # print the minimum
    print("Minimum:", "$",  format(min(pricesList), ",.2f")  )
   
    # print the maximum
    print("Minimum:", "$",  format(max(pricesList), ",.2f"))
   
    # print the total
    print("Total:", "$",  format(sum(pricesList), ",.2f"))
   
    # print the average. average = total/count
    average = sum(pricesList)/len(pricesList)
    print("Average:", "$",  format(average, ",.2f"))
   
    # print the median
    median = getMedian(pricesList)
    print("Median:", "$",  format(median, ",.2f"))
   
    # print the commission. commission = total * 0.03
    commission = sum(pricesList) * 0.03
    print("Commission:", "$",  format(commission, ",.2f") )
   

main()
