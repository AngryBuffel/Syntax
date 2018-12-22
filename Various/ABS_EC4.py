# VDLS - Automate the Boring Stuff with Python - Excercises Chapter 4
# 1.- What is []?
#       - It's an empty array.
# 2.- How would you assign the value 'hello' as the third value in a list stored
#     in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
#       - spam[2] = 'hello'
#For the following three questions, let’s say spam contains the list ['a','b','c','d'].
# 3.- What does spam[int(int('3' * 2) / 11)] evaluate to?
#       - spam[3] = d
# 4.- What does spam[-1] evaluate to?
#       - spam[-1] = d
# 5.- What does spam[:2] evaluate to?
#       - spam[:2] = ['a', 'b']
# For the following three questions, bacon = [3.14, 'cat', 11, 'cat', True].
# 6.- What does bacon.index('cat') evaluate to?
#       - bacon.index('cat') = 1
# 7.- What does bacon.append(99) make the list value in bacon look like?
#       - bacon = [3.14, 'cat', 11, 'cat', True, 99]
# 8.- What does bacon.remove('cat') make the list value in bacon look like?
#       - bacon = [3.14, 11, 'cat', True, 99]
# 9.- What are the operators for list concatenation and list replication?
#       - concatenation, replication = ['+', '*']
# 10.- What is the difference between the append() and insert() list methods?
#       - .append() method adds the argument to the end of the list,
#         .insert() method can insert a value at any index in the list.
# 11.- What are two ways to remove values from a list?
#       - del statement will delete values at an index in a list,
#         .remove() method is passed the value to be removed from the list it is called on.
# 12.- Name a few ways that list values are similar to string values.
#       - Both can be accessed by index number, concatenated and replicated.
# 13.- What is the difference between lists and tuples?
#       - Lists can be modified tuples can not.
# 14.- How do you type the tuple value that has just the integer value 42 in it?
#       - tuple = (42)
# 15.- How can you get the tuple form of a list value? 
#      How can you get the list form of a tuple value?
#       - tuple(list['item0', ..., 'itemN']) // list[tuple('item0', ..., 'itemN')]
# 16.- Variables that “contain” list values don’t actually contain lists directly.
#      What do they contain instead?
#       - They contain a reference to the list
# 17.- What is the difference between copy.copy() and copy.deepcopy()?
#       - .deepcopy() copies lists within a list, .copy() only copies the first list
# ---------------------------------------------------------------------------------------
# Comma Code
# Write a function that takes a list value as an argument and returns a string with all
# the items separated by a comma and a space, with 'and' inserted before the last item.

test_list = ['Spassky', 'Mikita', 'Domino', 'Kaito', 'Capablanca', 'Tigran']

def string_concatenator(anylist):
    for item in anylist:
        counter = 0
        for letter in item:
            if counter < len(item)-2:
                print(letter + ', ', end = '')
                counter += 1
            elif counter < len(item)-1:
                print(letter  + ' ', end = '')
                counter += 1
            else:
                print('and ' + letter + '.')

string_concatenator(test_list)

# Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def rotate_matrix(anymatrix):
    for y in range(6):
        for x in range(9):
            if x < 8:
                print(grid[x][y], end='')
            else:
                print(grid[x][y])

rotate_matrix(grid)