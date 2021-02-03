
# A tuple can also be created without using parentheses. This is known as tuple packing.

def packingUnpacking():
    my_tuple = 3, 4.6, "dog"
    print(my_tuple)

    # tuple unpacking is also possible
    a, b, c = my_tuple

    print(a)      # 3
    print(b)      # 4.6
    print(c)      # dog

packingUnpacking()
