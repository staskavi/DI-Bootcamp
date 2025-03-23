# Perfect number

# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

#     Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
#     Hint: Google perfect numbers

# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
print("Please enter a positive number...")
number = int(input())
while(int(number)<1):
    print("Number must be positive integer! Please enter a number...")
    number = int(input())
divisors_sum = 0
for x in range(number-1):
    if(number%(x+1) == 0):
        divisors_sum+=(x+1)
    if((divisors_sum == number) and ((x+1) == (number-1))):
        print("True")
        break
else: print("False")    


