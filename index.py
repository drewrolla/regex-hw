# # whiteboard of the day
# Fizz Buzz
# Given a random number as an input to a function, 
# return "FIZZ" if the number is even and "BUZZ" if the number is odd

def fizzBuzz(num):
    if num % 2 == 0:
        return "FIZZ"
    elif num % 2 != 0:
        return "BUZZ"

print(fizzBuzz(6))

# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number

def fizzBuzz2(num):
    if num % 3 == 0 and num % 5 == 0: # both parts need to be full conditionals
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num

print(fizzBuzz2(15))
