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
import random
list_float_int = []
i = 1
j = 0.5
while i<10:
    if((j+0.5).is_integer()):
        list_float_int.insert(i,int(j+0.5))
    else:
       list_float_int.insert(i,j+0.5)
    j+=0.5
    i += 1
print(list_float_int)