# VDLS - 11/12/18 - Excersices Chapter 2
# 2-1 Simple Message
msg = 'Plain text'
print(msg)
# 2-2 Simple Messages
msg = 'New message'
print(msg)
# 2-3 Personal Messages
name = 'david'
msg = 'Hello ' + name.title() + ', would you like to learn some Python today?\n'
print(msg)
# 2-4 Name Cases
cases = name.lower() + ' ' + name.upper() + ' ' + name.title()
print(cases) 
# 2-5-6 Famous Quote 1&2
famous_person = 'eric matthes'
part1 = ' once said, "Find a quote from a famous person you admire.\n'
part2 = ' Print the quote and the name of its author."\n'
msg = famous_person.title() + part1 + part2
print(msg)
# 2-7 Stripping names
strippedname = '\t blue whale\n'
print(strippedname.title())
print(strippedname.lstrip())
print(strippedname.rstrip())
print(strippedname.strip())
# 2-8 Number Eight
print(2+2+2+2)
print(1993-1985)
print(1*8)
print(32/4)
# 2-9 Favorite Number
f_numb = 12
print('My favorite number is ' + str(f_numb) + '.\n')
# 2-10 Adding Comments
# At the top