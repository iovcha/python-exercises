#Игра Fizz-Buzz
#for n in range(1, 101):
#    match n % 3, n % 5:
#        case 0, i if i > 0: print(f'{n} Fizz')
#        case i, 0 if i > 0: print(f'{n} Buzz')
#       case 0, 0: print(f'{n} FizzBuzz')
#        case _: print(n)

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('Fizz-Buzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)