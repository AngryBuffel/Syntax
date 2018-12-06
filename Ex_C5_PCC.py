# VDLS - 11/25/18 - Excercises Chaper 5 Python Crash Course
# 5.1 - Conditional tests.
import random
alien_color = ['green','red','blue','yellow','magenta','cyan']

def rand_pick(colors):
    # Generates a random index to pick a color.
    return colors[random.randint(0,len(colors))]

#print(alien_pick(alien_color))
score = 0
print('Do you want to choose an alien color? y/n \n')
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
    choice = input('Do you want to choose another alien color? y/n')