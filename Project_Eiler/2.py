#Progject Euler.
#The sum of all even fibonacci numbers up to 4 million.

#Creation fibonacci number.

#Необходимо написать фибоначи процедурнм кодом.
def fibonacci(max_count):
    #max_count = 10
    count = 0
    first, second = 0, 1

    while count < max_count:
        count += 1
        first, second = second, first + second

def fib():
    for number in fibonacci(10):
        print(number)

fib()