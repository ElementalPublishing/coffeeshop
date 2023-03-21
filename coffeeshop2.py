#Let's start a coffee shop!!!

#Lets build a robot barista!!!

print("Hello, welcome to the coffee shop!!!!!")

name = input("What is your name?\n")

menu = "Black Coffee, Espresso, Latte, Cappucchino\n" 


if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    import time
    time.sleep(6) # Wait for 6 seconds
else:
    print("\n\n\n\n\n\n" + "Hello " + name.capitalize() + ", Thank you for coming in today!!\n\n\n ")
    print(name.capitalize() + ", what would you like from our menu today? Here is what we are serving.\n\n" + menu + "\n")
    order = input()

    price = 8

    quantity = input("How many " + order.lower() + "s" + " would you like?\n")

    total = price * int(quantity)



    print("\n" + "Thank you " + name.capitalize() + ", your total is: $" + str(total) + "\n\n\n"
           + "We'll have your " + quantity + " " + order.lower() + "s" + " ready for you in a jiffy!")


    while True:
        user_input = input("(type 'thank you' to exit): ")
        if user_input == "thank you":
             break
    print("Thanks for stopping by!")
    import time
    time.sleep(6) # Wait for 6 seconds
