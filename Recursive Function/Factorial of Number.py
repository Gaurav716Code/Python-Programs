def factorial(n):
    assert n >= 0
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)


num=5

if num < 0:
    print('Factorials for negative number does not exist')
elif num == 0:
    print('Factorial of 0 is 1')
else:
    print('Factorial of ', num, 'is ',factorial(num))

print('F113 Gaurav Vishwakarma')
