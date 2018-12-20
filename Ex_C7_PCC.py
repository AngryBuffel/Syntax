# VDLS - 12/18/18 - Excercises Chaper 7 Python Crash Course
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