def createTuple():
    # Different types of tuples

    # Empty tuple
    my_tuple = ()
    print("Empty : ",my_tuple)

    # Tuple having integers
    my_tuple1 = (1, 2, 3)
    print("Integer : ",my_tuple1)

    # tuple with mixed datatypes
    my_tuple2 = (1, "Hello", 3.4)
    print("Mixed : ",my_tuple2)

    # nested tuple
    my_tuple3 = ("mouse", [8, 4, 6], (1, 2, 3))
    print("Nested : ",my_tuple3)

    #Having one element within parentheses is not enough.
    #We will need a trailing comma to indicate that it is, in fact, a tuple
    my_tuple4 = ("hello")
    print(type(my_tuple4))  # <class 'str'>
    print(my_tuple4)

    # Creating a tuple having one element
    my_tuple5 = ("hello",)
    print(type(my_tuple5))  # <class 'tuple'>
    print(my_tuple5)

    # Parentheses is optional
    my_tuple6 = "hello",
    print(type(my_tuple6))  # <class 'tuple'>
    print(my_tuple6)
    

createTuple()
