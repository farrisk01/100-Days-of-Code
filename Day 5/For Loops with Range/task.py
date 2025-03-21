

#The Gauss Challenge
#Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
# _sum = 0
# for i in range(1,101):
#     _sum += i
#
# print(_sum)


#FizzBuzz: Print all numbers between 1 & 100 except when the number is divisible by 3
# then print Fizz and print 5 when divisible by 5.

for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print(f'{i} = FizzBuzz')
    elif i % 3 == 0:
        print(f'{i} = Fizz')
    elif i % 5 == 0:
        print(f'{i} = Buzz')
    else:
        print(f'{i} = {i}')
