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

# size = input("Please, enter a size...")
# txt = input("Please, enter a message you want on a T-shirt...")
# make_shirt(size, txt)

# Exercise 6 : Magicians …
# Instructions

# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

#     Create a function called show_magicians(), which prints the name of each magician in the list.
#     Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
#     Call the function make_great().
#     Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
     for names in magician_names:
      print(names)
show_magicians(magician_names)

def make_great(magician_names):
    i = 0
    for names in magician_names:
        names += " the Great"
        magician_names[i] = names
        i+=1
make_great(magician_names)
show_magicians(magician_names)

#  Exercise 7 : Temperature Advice
# Instructions

#     Create a function called get_random_temp().
#         This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#         Test your function to make sure it generates expected results.


#  import random
# def get_random_temp():
#     temp_celcius = random.randint(-10, 40)
#     return temp_celcius

#     Create a function called main().
#         Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#         Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# def main():
#   temp_celcius = get_random_temp()
#   print(f"The temperature right now is {temp_celcius} degrees Celsius.")
# main()

#     Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#         below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#         between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#         between 16 and 23
#         between 24 and 32
#         between 32 and 40

# def main():
#   temp_celcius = get_random_temp()
#   if(temp_celcius<0):
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.'\n'Brrr, thats freezing! Wear some extra layers today")
#   elif(temp_celcius>-1 and temp_celcius<16):
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.'\n'Quite chilly! Dont forget your coat")
#   elif(temp_celcius>15 and temp_celcius<23):
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")    
#   elif(temp_celcius>22 and temp_celcius<32):
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")   
#   elif(temp_celcius>31 and temp_celcius<41):
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")       
# main()

#     Change the get_random_temp() function:
#         Add a parameter to the function, named ‘season’.
#         Inside the function, instead of simply generating a random number between -10 and 40, 
#         set lower and upper limits based on the season, eg. 
#         if season is ‘winter’, temperatures should only fall between -10 and 16.
#         Now that we’ve changed get_random_temp(), let’s change the main() function:
#             Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. 
#           Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#             Use the season as an argument when calling get_random_temp().

# import random
# def get_random_temp(season):
#      if(season == 'winter'):
#       temp_celcius = random.randint(-10, 16)
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")
#      elif(season == 'spring'): 
#       temp_celcius = random.randint(0, 22)
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")
#      elif(season == 'summer'):
#       temp_celcius = random.randint(22, 40)
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.") 
#      elif(season == 'fall'):
#       temp_celcius = random.randint(0, 22)
#       print(f"The temperature right now is {temp_celcius} degrees Celsius.")

# def main():
#     input_season = input("Please, type in a season...(winter, spring, summer or fall)...")
#     season = input_season.lower()
#     if((season != 'winter') and (season != 'spring') and (season != 'summer') and (season != 'fall')):
#         print("ERROR! Input must be winter, spring, summer or fall!")
#     get_random_temp(season)
# main()        

#     Bonus: Give the temperature as a floating-point number instead of an integer.

import random

def get_random_temp():
    temp_celcius = round(random.uniform(-10,40), 2)
    return temp_celcius
def main():
  temp_celcius = get_random_temp()
  print(f"The temperature right now is {temp_celcius} degrees Celsius.")
main()

# Exercise 8 : Star Wars Quiz
# Instructions

# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives
#  different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

    # 1.Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
    # 2.Create a function that informs the user of his number of correct/incorrect answers.
    # 3.Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
    # If he had more then 3 wrong answers, ask him to play again.

def questions(data):
    correct_answers = 0
    incorrect_answers = []
    right_answers = []
    for key, val in enumerate(data):
        print(val["question"])
        answer = input("Type your answer...")
        answer_capitalize = answer.capitalize()
        if(answer_capitalize == val["answer"]):
            correct_answers+=1
            print(f"Correct. You get {correct_answers} points")
        else:
            print(f"Wrong answer")
            right_answers.append(val["answer"])
            incorrect_answers.append(answer_capitalize)
    print(f"Quiz is finished! You get {correct_answers} points")
    print(f"Your wrong answers are: {incorrect_answers}")
    print(f"The right answers was: {right_answers}")
    if(len(incorrect_answers)>3):
        print("Play Again")


questions(data)


