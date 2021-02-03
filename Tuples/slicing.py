def slicing():
    # Accessing tuple elements using slicing
    my_tuple = ('p','r','o','g','r','a','m','i','z')
    print(my_tuple)

    # elements 2nd to 4th
    # Output: ('r', 'o', 'g')
    print("slicing range [1:4] : ",my_tuple[1:4])

    # elements beginning to 2nd
    # Output: ('p', 'r')
    print("slicing range [:-7] : ",my_tuple[:-7])

    # elements 8th to end
    # Output: ('i', 'z')
    print("slicing range [7:] : ",my_tuple[7:])

    # elements beginning to end
    # Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    print("slicing range [:] : ",my_tuple[:])

slicing()
