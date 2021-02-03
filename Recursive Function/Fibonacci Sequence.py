def fib(n):
    if n <= 1:
        return 1
    else:
        return(fib(n-1) + fib(n-2))

num = 10

if num <= 0:
    print('Please enter a positive integer')
else:
    print('Fibonacci sequence: ')
    for i in range(num):
        print(fib(i))
print('F113 Gaurav Vishwakarma')
