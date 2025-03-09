#Exercise 1 : Hello World
#Instructions

#Print the following output in one line of code:

#Hello world
#Hello world
#Hello world
#Hello world
print("Hello world "+"Hello world "+"Hello world "+"Hello world "+"Hello world ")
print("Hello world","Hello world","Hello world","Hello world","Hello world")
hw = "Hello world "
print(hw*5)

#Exercise 2 : Some Math
#Instructions

#Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)

#Exercise 3 : What is the output ?
#Instructions

#Predict the output of the following code snippets:

#>>> 5 < 3

#>>> 3 == 3

#>>> 3 == "3"

#>>> "3" > 3

#>>> "Hello" == "hello"
print(bool(5 < 3))
print(bool(3 == 3))
print(bool( 3 == "3"))
print(bool("Hello" == "hello"))

#Exercise 4 : Your computer brand
#Instructions

#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable print a sentence that prints the following: "I have a <computer_brand> computer".
computer_brand = "HP"
print("I have a "+ computer_brand + " computer")

#Exercise 5 : Your information
#Instructions

#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
#Have your code print the info message.
#Run your code
name = "Stas"
age = str(39)
shoe_size = str(43)
info = "Hi! My name is "+name+ " My age is "+age+ " and my boots are "+shoe_size+" size!"
print(info)

#Exercise 6 : A & B
#Instructions

#Create two variables, a and b.
#Each variable value should be a number.
#If a is bigger then b, have your code print Hello World.
a = 100
b = 10
if (a>b):
    print("Hello world!")
else :
    print("Bye!")

#Exercise 7 : Odd or Even
#Instructions

#Write code that asks the user for a number and determines whether this number is odd or even.
print("Please, enter number...")
num = int(input())
if(num%2==0):
    print("Your number "+str(num)+" is even")
else: print("Your number "+str(num)+" is odd")    

#Exercise 8 : What’s your name ?
#Instructions

#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
print("Please enter your name...")
user_name = input()
my_name = "Stas"
if(my_name.upper()==user_name.upper()):
    print("Congratulations! We have the same name - "+user_name)
else: print("Try again")

#Exercise 9 : Tall enough to ride a roller coaster
#Instructions

    #Write code that will ask the user for their height in centimeters.
    #If they are over 145cm print a message that states they are tall enough to ride.
    #If they are not tall enough print a message that says they need to grow some more to ride.
print("Please enter your height in centimeters...")
user_height = int(input())
if(user_height>145): print("You are tall enough to ride!")
else: print("You need to grow some more to ride!")

