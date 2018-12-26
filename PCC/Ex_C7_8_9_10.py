# VDLS - 12/18/18 - Excercises (7.8/7.9/7.10) Chapter 7 Python Crash Course
# 7.8 Deli / 7.9 No Pastrami
sandwich_orders = ['pastrami', 'tuna', 'ham', 'pastrami', 'meatballs', 'cheese', 'pastrami', 'italian', 'blt']
finished_sandwiches = []

# TODO: Change pastrami for a var, so any kind of sandwich can be removed from list.
if 'pastrami' in sandwich_orders:
    print("\nSorry! Deli has no Pastrami left...\n")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    making = sandwich_orders.pop()

# This might be more efficient since we are going to cycle through the list anyway.
#    if making == 'pastrami':
#        print("Sorry! Deli has no Pastrami left...")
#        continue
    
    print("I am making your " + making.title() + " sandwich")
    finished_sandwiches.append(making)

print("\n----Finished Sandwiches-----\n")
for sandwich in finished_sandwiches:
    print("A " + sandwich.title() + " sandwich was made.")