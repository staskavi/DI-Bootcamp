# Challenge 1

#     Ask the user for a number and a length.
#     Create a program that prints a list of multiples of the number until the list length reaches length.

print("Enter number...")
user_num = int(input())
print("Enter length...")
user_len = int(input())
user_list = []
multiple_user_num = user_num
while(user_len):
    user_list.append(multiple_user_num)
    multiple_user_num += user_num
    user_len-=1
print(user_list) 

# Challenge 2

#     Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).   
print("Enter string...")
user_str = input()
formatted_str = ""
user_list = list(user_str)
new_list = []
new_list.append(user_list[0])
i = 0
j=0
k=len(user_str)-1
while(k):
     if(new_list[j]!=user_list[i+1]):
         new_list.insert(j+1,user_list[i+1])
         j+=1
     i+=1
     k-=1
formatted_str =  "".join(new_list)   
print(formatted_str)


