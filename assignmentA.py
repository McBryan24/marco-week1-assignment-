
#2. Create a tuple of 5 city names. Attempt to change one and explain what happens.
cities = ("Nairobi", "Accra", "Brussels", "Lagos", "Windhoek")
cities_copy = ["Nairobi", "Accra", "Brussels", "Lagos", "Windhoek"]

#3. Create a set of student names. Add a duplicate and observe what happens.
student_names = {"Brenda", "Latisha", "Linda", "Felicia", "Dawn", "LeShaun", "Alicia"}
student_names.add("Brenda")
print(student_names)

#4 Create a dictionary storing a person's name, age, and email.
# Update the email and print all keys and values.
particulars = {"name":"Brian", "age":29, "email":"stingray@hhs.gov"}
particulars.update({"email":"sturgeon@state.gov"})
print(particulars)

#Part B: Control Flow
#1. Write a loop that prints whether each number from 1 – 20 is odd or even.
for number in range(21):
    if number % 2 == 0:
        print( str(number) + " is even" )
    else:
        print(str(number) + " is odd" )

#2. Use a for loop to iterate over a dictionary (from Part A) and print keys and values.
for aspects in particulars.items():
    print (aspects)

#3. Write a program that checks if a student’s grade (0–100) is:
# - A: 80+ - B: 70–7 - C: 60–69 - D: 50–59 - F: < 50
stdt_grade = int(input("Enter student's grade:"))
if stdt_grade >= 80:
    print("Grade A")
elif stdt_grade >= 70:
    print("Grade B")
elif stdt_grade >= 60:
    print("Grade C")
elif stdt_grade >= 50:
    print("Grade D")
else:
    print("Grade F")

#Part C: Functions and Modular Code
#1 .Define a function calculate_mean() that takes a list of numbers and returns the mean.
def calculate_mean(nums):
    if not nums:            #checking if list is emptyy
        return 0
    else:
        return sum(nums)/len(nums)
#nums = [1,2,3,4,5,6,7,8,9,10] ---Testing the fnction with sample list
#print(calculate_mean(nums)) ---returns 5.5

#2 Create a module file (utils.py) with at least two functions:
#- greet_user(name)
#- square_number(n)
#- Import and use those functions in your main script.

#from utils import greet_user, square_name
import utils
greet_user('Marco')
square_name(3)
print(square_name(3))

#Part D: Error Handling
try:
    m = int(input("Enter first number:"))
    n = int(input("Enter second number:"))
    result = m/n
except ZeroDivisionError:
    print("Division by zero detected")
except ValueError:
    print("ValueError detected")
else:
    print("Result:", result)
finally:
    print("Division Complete!")


