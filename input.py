#Input() = A function that prompts the user to enter data
#          Returns the entered data as a sting

name = input ("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}, how are you today!")
print(f"HAPPY BIRTHDAY {name}🥳🎂!")
print(f"You are now {age} years old🎉✨")


#Exercise 1 Rectangle Area Calc

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area}cm²")



#Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"The will be ${total}, cash💵 or card💳?😊")