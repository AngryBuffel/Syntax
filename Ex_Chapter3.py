# VDLS - 11/12/18 - Excersices Chapter 3

    # 3-1 Names
roomies = ['Eliezer','Luis','David']
for i in range(0,3):
    print(roomies[i])

    # 3-2 Greetings
for i in range(0,3):
    print('Greetings ' + roomies[i] + ', such a nice day!')

    # 3-3 Your Own List
cars = ['lexus','audi','BMW','mercedes benz','volvo','rolls royce']
for i in range(0,6):
    print('I look fancy as fuck while driving my ' + cars[i].title() + '!')

    # 3-4 Guest List
guests = ['Edzard','Tano','Alvaro','Caro','Ambriz','Gustavo','Fer']
for x in guests:
    msg = '!, I want to invite you to a dinner'
    print(x + msg)
    
    # 3-5 Changing guest list
guests.remove('Edzard')
print('Oh no, Edzard can not go!')
for x in guests:
    new_msg = 'I hope you can still go to dinner '
    print(new_msg + x)

    # 3-6 More Guests
print('Hey guys, I found  a bigger table!\n')
guests.insert(0,'Eliezer')
guests.insert(3,'Spassky')
guests.append('Leibniz')
for x in guests:
    new2_msg = ' I found a bigger table, hope you can make it...'
    print('Hi ' + x + new2_msg)
    if x == 'Leibniz':
        print('\n')

    # 3-7 Shrinking Guest List
print("I wasn't able to get the big table :c \n")
g_going = []
for guest in guests:
    if guest == 'Tano' or guest == 'Spassky':
        g_going.append(guests.pop(guests.index(guest)))
for i in range(0,len(guests)):
    print('Sorry ' +  guests.pop() + ", you can't go to dinner.")

print(guests)

    # 3-8 Seeing the World
places = ['madagascar','burkina faso','rusia','japon','alemania']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

    # 3-9 Dinner Guests
print("I'm inviting " + str(len(g_going)) + " friends to my dinner.")

    # 3-10 Every Function
#.append() // .insert() // del // .pop() // .remove() // .sort() // sorted() // reverse() // len()
lol_adcs = ['caitlyn','miss fortune','twich','jhin','lucian','sivir']
