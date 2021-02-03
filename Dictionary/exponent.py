# Program to make a dictionary with each item being a pair of a number given as input by user and its square
def sqDict():
    print("~~~~~Program to create dictionary of squares of numbers ~~~~~")
    limit = int(input("Enter a limit : "))
    power = int(input("Enter power : ")) 
    # Dictionary Comprehension
    squares = {num: num*power for num in range(limit)}

    print(squares)

sqDict()
