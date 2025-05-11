#2. Create a tuple of 5 city names. Attempt to change one and explain what happens.
cities = ("Nairobi", "Accra", "Brussels", "Lagos", "Windhoek") #Tuple of city names
#cities.append("Kampala") #this line of code returns an error - immutability features of tuples don't allow for modification of data
cities_copy = ["Nairobi", "Accra", "Brussels", "Lagos", "Windhoek"] #a list of city names allows for changes - mutability
cities_copy.append("Kampala")
print(cities_copy)