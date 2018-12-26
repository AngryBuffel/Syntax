# VDLS - 12/18/18 - Excercises Chapter 7 Python Crash Course
# 7.1 Rental Car
car_model = input('Which car brand would you like to use?: ')
print('Let me see if I can find you a ' + car_model.title() + '.')
# 7.2 Restaurant Seating
people_num = input('How many people are in your dinner group?: ')
people_num = int(people_num)
if people_num > 8:
    print("You'll have to wait for a table...")
else:
    print("Your table is ready!")
#7.3 Multiples of ten
user_num = input("Please enter an integer number: ")
user_num = int(user_num)
num_ck = user_num % 10
while num_ck != 0:
    not_ten = input("Your number is not a multiple of ten \n Would you like to try again (Y, N)?")
    not_ten = not_ten.lower().strip()
    if not_ten == 'y':
        user_num = input("Please enter an integer number: ")
        user_num = int(user_num)
    else:
        break
# 7.4 Pizza toppings / 7.6 Three exits
pizza_tops = []
active = True
prompt = '\n Please enter the toppings you would like on your pizza: '
prompt += "\n (Enter 'quit' when you are finished.)"

while active:
    message = input(prompt)
    pizza_tops.append(message)
    print(pizza_tops)
    if message == 'quit':
        active = False
        # break
    else:
        print(message)

# 7.7 Infinity
# This is an infite loop crtl+c to stop
infite = True
while infite:
    print("This is an infinite loop")