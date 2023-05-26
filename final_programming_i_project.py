# -*- coding: utf-8 -*-
"""Final Programming-I Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVdG7M79D0VrJTQIp2chmrWnwPZ9hLYw
"""

import matplotlib.pyplot as plt

def option1(inList):        #Ex. 6,7,8 ch. 
  print("This is option 1")
  year = int(input("Please enter year: "))
  while year > 1990 or year < 1950:
    print("Error: Input is incorrect.")
    year = int(input("Enter the value: "))
  print(f"Population in year {year}: {inList[year-1950]:,}") 

def option2(inList):
  print("This is option 2")
  year1 = int(input("Enter first year: "))
  year2 = int(input("Enter second year: "))
  difference = inList[year2-1950] - inList[year1-1950]  #  inList[year2-1950] will give population at index of year2
  print(f"The change in population between the two years is: {difference:,}")

def option3(inList):
    start = int(input("Please enter the first year: ")) - 1950
    end = int(input("Please enter the second year: ")) - 1950 
     
    total = 0 # calculate total
    for i in range(start,end+1):
        total += inList[i]
    avg = total/((end+1)-start) #calculate average 
    print(f"The average is: {avg:3,.2f} ")

def main():
  toContinue = True #this boolean controlls the loop
  popList = [ ] #use this variable for the list of population values
    
  # Open and read in file USPopulation.txt. Convert the values to int, and multiply
  # by 1000 to expand to full amount.

  file = open("USPopulation1.txt","r")
  
  for line in file:
     # if len(popList) > 41:
     #   print("Error. The input file containts values outside the range.")

      popList.append(int(line.split()[0]) * 1000)

  #file.close()

  while toContinue:
    #display the menu
    print()
    print("Please select one of the following options: ")
    print("1 - Display population for selected year")
    print("2 - Display change in population between two values")
    print("3 - Display the average population for range between two values")
    print("6 - Exit")

    choice = input("Select an option:")

    if choice==str(1):
      option1(popList)
    elif choice==str(2):
      option2(popList)
    elif choice==str(3):
      option3(popList)
    else:
      print("The program is exiting.")
    toContinue= False

main()

