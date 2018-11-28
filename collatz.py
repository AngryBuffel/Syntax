def collatz(number):
    evenodd =  number % 2
    if evenodd == 0:
        return number // 2
    else:
        return 3 * number + 1
  
while True:
    try:
        print('Please introduce an integer number')
        number = int(input())
        break
    except ValueError:
        print('Error: Only integers are allowed.\n')

while collatz(number) != 1:
    number = collatz(number)
    print(collatz(number))