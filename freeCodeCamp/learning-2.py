num_one = 19

num_two = 9

if num_one < num_two: # < means Less then
    print('NO the number is less')
elif num_one > num_two:  # = Greater then
    print("YES the number is greater")
else:
    print("I don't care that much about math")



name = "Alice"

age = 18

if age >= 18:  # >= means Greater or equal to
    print(f"Happy birthday🥳🎂 {name}, you have finally become an adult")
elif age <= 17:  # <= means Less or equal to
    print(f"Sorry {name}, you aren't old enough yet to join the party, just wait one more year")
else:
    print("You are kid go back home kiddo")


if name != 'Alice':   # != means NOT equal
    print(f'You are NOT {name}')
elif name == 'Alice':   # == means Equal to
    print(f'Hey {name}, welcome back')
else:
    print('Who are you?')



# Nested conditional statements

is_citizen = True

age = 20

if is_citizen:
    if age >= 18:
        print("You are eligible to vote")
else:
    print("You are not eligible to vote")


Name = 'Jack'
have_birthday = True
Age = 26
Age += 1

if Name == 'Jack':
    if have_birthday:
        print(f'Happy birthday {Name}, You are finally {Age} years old')
else:
    print(f"It's not your birthday yet {Name}")