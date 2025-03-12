# Exercise 1 : Favorite Numbers
# Instructions
#     Create a set called my_fav_numbers with all your favorites numbers.
#     Add two new numbers to the set.
#     Remove the last number.
#     Create a set called friend_fav_numbers with your friend’s favorites numbers.
#     Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers = {1, 5, 7, 13, 17, 26}
print(my_fav_numbers)
my_fav_numbers.add(10)
my_fav_numbers.add(0)
print(my_fav_numbers)
my_fav_numbers = set(list(my_fav_numbers)[:-1])
print(my_fav_numbers)
friend_fav_numbers = {1, 5, 7, 13, 17, 26}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
#Answer is NO. You can't add int to tuple

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#     Remove “Banana” from the list.
#     Remove “Blueberries” from the list.
#     Add “Kiwi” to the end of the list.
#     Add “Apples” to the beginning of the list.
#     Count how many apples are in the basket.
#     Empty the basket.
#     Print(basket)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.insert(len(basket),"Kiwi")
print(basket)
basket.insert(0,"Apples")
print(basket)
basket_set = set(basket)
print(len(basket)-len(basket_set))
counter = 0
for i in basket:
    if (i =="Apples"):
     counter+=1
print("Amount of apples in basket are: "+str(counter))
basket.clear()
print(basket)
#  Exercise 4: Floats
# Instructions
#     Recap – What is a float? What is the difference between an integer and a float?
#     Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#     Can you think of another way to generate a sequence of floats?

list_float_int = []
i = 1
j = 0.5
while i<40:
    if((j+0.5).is_integer()):
        list_float_int.insert(i,int(j+0.5))
    else:
       list_float_int.insert(i,j+0.5)
    j+=0.5
    i += 1
print(list_float_int)
# Exercise 5: For Loop
# Instructions
#     Use a for loop to print all numbers from 1 to 20, inclusive.
#     Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for num in range(len(list_float_int)):
    print(list_float_int[num])

for num in range(len(list_float_int)):
   if((num%2)==0):
      print(list_float_int[num])
# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
my_name = "Stas"
your_name = ""
while(1):
     if(your_name.upper() == my_name.upper()):
      print("Great! We have the same name")
      break
     else:
       print("Enter your name:")
       your_name = input()

# Exercise 7: Favorite fruits
# Instructions
#     Ask the user to input their favorite fruit(s) (one or several fruits).
#     Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#     Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#     Now that we have a list of fruits, ask the user to input a name of any fruit.
#         If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#         If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

favorite_fruits = ""
print("Input your favorite fruit(s) (one or several fruits), please, separate the fruits with a single space...")
favorite_fruits = input()
print(favorite_fruits)
favorite_fruits_list = favorite_fruits.split()
print(favorite_fruits_list)
print("Input a name of any favorite fruit...")
favorite_fruit = input()
if (favorite_fruit in favorite_fruits_list):
   print("You chose one of your favorite fruits! Enjoy!")
else:
   print("You chose a new fruit. I hope you enjoy")


#    Exercise 8: Who ordered a pizza ?
# Instructions
#     Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#     As they enter each topping, print a message saying you’ll add that topping to their pizza.
#     Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).
# quit_word = "quit"
# your_input = ""
# topping_list = []
# topping_counter = 0
# loop_counter = 0
# total_price = 0
# while(1):
#      if(your_input.upper() == quit_word.upper()):
#       print("All the toppings you choose are:")
#       topping_list= topping_list[:-1]
#       print(topping_list)
#       total_price = ((topping_counter-1)*2.5)+10
#       print("Total price is "+ str(total_price))
#       break
#      else:
#        print("Enter pizza topping")
#        your_input = input()
#        topping_list.insert(loop_counter,your_input.split())
#        loop_counter+=1
#        topping_counter+=1

#    Exercise 9: Cinemax
# Instructions
#     A movie theater charges different ticket prices depending on a person’s age.
#         if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.
#     Ask a family the age of each person who wants a ticket.
#     Store the total cost of all the family’s tickets and print it out.
#     A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#     Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#     At the end, print the final list.


# print("How old are you?")
# age = input()
# clients_age_list = []  #didn't understand structure of list. Is it must include names and ages? When program should stop asking the age?  What is " Given a list of names"?
# # where is it? not clear at all
# total_tickets_price = 0
# if(age < 3):
#  total_tickets_price+=0
# elif(age>3 and age <12):
#    total_tickets_price+=10
# else:
#    total_tickets_price+=15 




# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :
# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

#     The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
#     We need to prepare the orders of the clients:
#         Create an empty list called finished_sandwiches.
#         One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#     After all the sandwiches have been made, print a message listing each sandwich that was made
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
run_out = "Pastrami sandwich"
print(sandwich_orders)
while(run_out in sandwich_orders):
   sandwich_orders.remove(run_out)
print(sandwich_orders) 
for i in range (len(sandwich_orders)):
 finished_sandwiches.append(sandwich_orders[i])

print(finished_sandwiches)
sandwich_orders.clear()
print(sandwich_orders)
for i in range(len(finished_sandwiches)):
   print("I made your ",finished_sandwiches[i])
