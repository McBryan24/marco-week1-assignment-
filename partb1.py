#Part B: Control Flow
#1. Write a loop that prints whether each number from 1 – 20 is odd or even.
for number in range(21):
    if number % 2 == 0:
        print( str(number) + " is even" )
    else:
        print(str(number) + " is odd" )