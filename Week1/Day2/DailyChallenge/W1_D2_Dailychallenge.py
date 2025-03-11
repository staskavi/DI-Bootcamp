#Daily challenge: Build up a string

#Using the input function, ask the user for a string. The string must be 10 characters long.

    #If it’s less than 10 characters, print a message which states “string not long enough”.
    #If it’s more than 10 characters, print a message which states “string too long”.
    #If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
print("Please enter a string. The string must be 10 characters long.")
user_string = input()
if(len(user_string)<10):
    print("string not long enough")
elif(len(user_string)>10):
    print("string too long")
else: print("perfect string")

# Then, print the first and last characters of the given text.
print(user_string[0])
print(user_string[len(user_string)-1])

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. 
new_string = ""
for char in user_string: 
    new_string+=char
    print(new_string)
    
# Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).
import random
list_user_string = list(user_string)
random.shuffle(list_user_string)
shuffle_string = ''.join(list_user_string)
print(shuffle_string)
