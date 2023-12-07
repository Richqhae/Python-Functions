#importing the math function math.pi
import math

#Printing description of my program to the user

print("This program computes and outputs")
print("the volume space inside a tire")

#Getting the diameter, aspect ratio and width
width = float(input("Enter the width of the tire: "))
aspect_ratio = input("Enter the aspect ratio of the tire: ")
diameter =input("Enter the diameter of the tire: ")

#Computing the volume of the tire

radiant = (int(width) * int(aspect_ratio)) +  int(2540* int(diameter))

volume = ((int(math.pi)) * (int(int(width)**2))) * int(aspect_ratio) * int(radiant) /int(10000000000)

#rounding the volume to a two decimal place
volume = round(volume, 2)

#Printing volume for user 

print(f"The volume of the space of the tire is {volume}")

#importing the dTE nd time function
from datetime import datetime
#Printing the date and time for user
current_date = datetime.now()
print("Today is " + str(current_date))

#Importing the open and append the file function
with open("volumes.txt", "at") as volumes:

#Printing the appended file

