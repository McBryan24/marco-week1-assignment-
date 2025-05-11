#Part C: Functions and Modular Code
#1 .Define a function calculate_mean() that takes a list of numbers and returns the mean.
def calculate_mean(nums):
    if not nums:            #checking if list is emptyy
        return 0
    else:
        return sum(nums)/len(nums)
#nums = [1,2,3,4,5,6,7,8,9,10] ---Testing the fnction with sample list
#print(calculate_mean(nums)) ---returns 5.5