#Let's start a coffee shop!!!

#Lets build a robot barista!!!

print("Hello, welcome to the coffee shop!!!!!")

name = input("What is your name?\n")

print("\n\n\n\n\n\nHello " + name + ", Thank you for coming in today!!\n\n\n ")

menu = "Black Coffee, Espresso, Latte, Cappucchino\n" 

print(name + ", what would you like from our menu today? Here is what we are serving.\n\n" + menu + "\n")

order = input()

print("Sounds good " + name + ", we'll have that " + order + " ready for you in a moment!")

import time

while True:
    user_input = input("(type 'thank you' to exit): ")
    if user_input == "thank you":
        break

print("Thanks for stopping by!")
time.sleep(6) # Wait for 6 seconds