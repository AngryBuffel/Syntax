# VDLS - 11/25/18 - Excercises Chaper 5 Python Crash Course
# 5.3 - 5.5 Alien Colors.
import random
alien_color = ['green','red','blue','yellow','magenta','cyan']

def rand_pick(colors):
    # Generates a random index to pick a color.
    return colors[random.randint(0,len(colors)-1)]

#print(alien_pick(alien_color))
score = 0
print('Do you want to choose an alien color? y/n')
choice = input()

while choice == 'y':
    if rand_pick(alien_color) == 'green':
        score += 5
        print('Alien was green, you win 5 points!')
    elif rand_pick(alien_color) == 'yellow':
        score += 10
        print('Alien was yellow, you win 10 points!')
    elif rand_pick(alien_color) == 'red':
        score += 15
        print('Alien was red, you win 15 points!')
    else:
        score += 7
        print('Alien was a custom color, you win 7 points!')
    print('Your score is ' + str(score) + ' points!')
    choice = input('Do you want to choose another alien color? y/n \t')

# 5.6 Stages of life

age = int(input('Please enter your age: '))

if age < 2:
    print('You are a baby!')
elif age < 4:
    print('You are a toddler!')
elif age < 13:
    print('You are a kid!')
elif age < 20:
    print('You are a teenager!')
elif age < 65:
    print('You are an adult!')
else:
    print('You are an elder!')

# 5.7 Favorite Fruit

favorite_fruit = ['grape','apple','avocado','lemon','mango','pear']
some_fruit = []
n_fruits = input('Enter how many fruits you want to check: ')
for i in range(int(n_fruits)):
    some_fruit.append(input('Please enter a fruit:\t'))

print(some_fruit)

# 5.9 No Users - Empty list check
if not some_fruit:
    print('We have no fruits!')

for fruit in some_fruit:
    # 5.8/5.10 Hello Admin - List item search
    if fruit in favorite_fruit:
        print('You really like ' + fruit + '!')
    else:
        print(fruit.upper() + ' is not one of your favorite fruits :(')