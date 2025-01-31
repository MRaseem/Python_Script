# if number is 15 output should be FizzBuzz,if output is divisble by 3 it should be Fizz and 5 buzz else the number

for n in range(101):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0 :
        print('Fizz')
    elif n % 5 == 0 :
        print ('Buzz')
    else :
        print(n)