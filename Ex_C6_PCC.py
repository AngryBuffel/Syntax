# VDLS - 12/06/18 - Excercises Chaper 6 Python Crash Course
# 6.1 - Person
person_1 = {
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
rivers = {
    'atoyac': 'oaxaca',
    'usumacinta': 'chiapas',
    'lerma': 'mexico',
    }
for n, c in rivers.items():
    print('The river ' + n.title() + ' is located in the state of ' + c.title())
# 6.6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'fer': 'html',
    'caro': 'javascript',
    }
poll_users = ['fer','jen','david','robert','caro','phil','edzard']
for user in poll_users:
    if user in favorite_languages.keys():
        print('Thank you ' + user.title() + ' for taking the poll.')
    else:
        print(user.title() + ' please take the poll.')
# 6.7 People
person_2 = {
    'first name': 'camila',
    'last name': 'orozco',
    'age': 18,
    'city': 'leon',
    }
person_3 = {
    'first name': 'yeya',
    'last name': 'killove',
    'age': 23,
    'city': 'leon'
    }
people = [person_1, person_2, person_3]
for person in people:
    for u, i in person.items():
        full_name = i['first name'] + " " + i['last name']
        