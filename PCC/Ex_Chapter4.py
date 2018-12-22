# VDLS - 11/15/18 - Excersices Chapter 4
    # 4-1 Pizzas
pizzas = ['pepperoni','cheese','meatlover']
for pizza in pizzas:
    print('I love eating '+ pizza + ' pizza!')

print('Very pizza')

    # 4-2 Animals
animals = ['cat','lion','cheeta','jaguar']

for animal in animals:
    print('A ' + animal + ' would make a great pet!')
print('\nAny of these animals would make a great pet!')
print('\n\t  If they dont eat you...')

    # 4-3 Counting to Twenty
counting =  list(range(1,21))
print(counting)

    # 4-4 One Million
paco_rabbane = list(range(1,1000001))

    # 4-5 Summing a Million
print(min(paco_rabbane))
print(max(paco_rabbane))
print(sum(paco_rabbane))

    # 4-6 Odd Numbers
odd_n = list(range(1,21,2))
print(odd_n)

    # 4-7 Threes
threes = [three for three in range(3,31,3)]
print(threes)

    # 4-8 Cubes
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

    # 4-9 Cube Comprehension
ccc = [cc**3 for cc in range(1,11)]
print(ccc)

    # 4-10 Slices
print('The first three items in the list are:')
for cc in ccc[:3]:
    print(cc)
print('Four items from the middle of the list are:')
for cc in ccc[3:7]:
    print(cc)
print('The last three items in the list are:')
for cc in ccc[-3:]:
    print(cc)

    # 4-11 My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('new')
friend_pizzas.append('different')
print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza.title() + ' pizza...')
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title() + ' pizza...')