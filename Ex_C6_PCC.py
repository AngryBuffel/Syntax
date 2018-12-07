# VDLS - 12/06/18 - Excercises Chaper 6 Python Crash Course
# 6.1 - Person
person = {
    'first_name': 'daniel',
    'last_name': 'aragon',
    'age': 25,
    'city': 'toluca',
    }
# 6.2 Favorite Numbers
favorite_N = {
    'daniel': 1,
    'ana': 2,
    'eliezer': 3,
    'camila': 4,
    'mafer': 5,
    }
# 6.3/6.4 Glossary
glossary = {
    'lambda_func': 'can take any number of arguments, but only one expression',
    'augmented_op': '+=,-=,*=,/=',
    'dictionary': 'stores objects and lists with custom keys',
    'boolean': 'true or false',
    }
# Looping Through All Key-Value Pairs 1
for key in glossary:
    print(key + ' can be defined as ' + glossary[key] + '.\n')
# Looping Through All Key-Value Pairs 2
for k, v in glossary.items():
    print(k + ' can be defined as ' + v)
# Looping Through All the Keys in a Dictionary
for item in glossary.keys():
    print(item.title())
# 6.5 Rivers
