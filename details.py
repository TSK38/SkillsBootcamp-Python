'''This is the pseudo code to Practical Task 2
Ask the user to input their name, age, house number and street name 
Print out all the details obtained in a single sentence, e.g. "This is John Smith. He is 28 years old and lives at house number 42 on Hamilton Street.'''

name = input("Please enter your full name: ")
age = input("Please enter your age: ")
house_number = input("Please enter your house number: ")
street_name = input("Please enter your street name: ")
details = f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}."
print(details)