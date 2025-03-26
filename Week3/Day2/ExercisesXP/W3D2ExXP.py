#  Exercise 1 : What are you learning ?
# Instructions

#     Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
#     Call the function, and make sure the message displays correctly.

def  display_message():
    print("I'm learning FullStack Web Programming!!!")
display_message()

#  Exercise 2: What’s your favorite book ?
# Instructions

#     Write a function called favorite_book() that accepts one parameter called title.
#     The function should print a message, such as "One of my favorite books is <title>".
#     For example: “One of my favorite books is Alice in Wonderland”
#     Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")

# Exercise 3 : Some Geography
# Instructions

#     Write a function called describe_city() that accepts the name of a city and its country as parameters.
#     The function should print a simple sentence, such as "<city> is in <country>".
#     For example “Reykjavik is in Iceland”
#     Give the country parameter a default value.
#     Call your function.
def describe_city(city, country ='Israel'):
    print(f"{city.capitalize()} is in {country.capitalize()}")
describe_city('reykjavik','iceland')

# Exercise 4 : Random
# Instructions

#     Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
#     Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# import random

# def my_rand(first_num):
#     if(first_num<1 or first_num>100):
#         print("ERROR! Number must be between 1 and 100")
#         pass
#     else:
#         second_num = random.randint(1, 100)
#         if(second_num == first_num):
#           print(f"Success!!! {first_num} equals {second_num}")
#         else:
#             print(f"Fail {first_num} NOT equal to {second_num}")
#             pass
# first_num = input("Please enter number between 1 to 100...")        
# my_rand(int(first_num))

#  Exercise 5 : Let’s create some personalized shirts !
# Instructions

#     Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#     The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#     Call the function make_shirt().


def make_shirt(size, txt):
    print(f"The size of the shirt is {size} and the text is '{txt}'")
make_shirt('XL', 'MetallicA')

#     Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#     Call the function, in order to make a large shirt with the default message
#     Make medium shirt with the default message
#     Make a shirt of any size with a different message.

def make_shirt(size = 'L', txt = 'I love Python'):
    print(f"The size of the shirt is {size} and the text is '{txt}'")
make_shirt()
make_shirt('M')
make_shirt('S', 'IDF')

#     Bonus: Call the function make_shirt() using keyword arguments.

size = input("Please, enter a size...")
txt = input("Please, enter a message you want on a T-shirt...")
make_shirt(size, txt)


          