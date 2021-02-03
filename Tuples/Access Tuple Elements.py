def acesselementindex():
    # Accessing tuple elements using indexing
    my_tuple = ('p','e','r','m','i','t')
    print(my_tuple)
    print("Accessing tuple elements using indexing : ",my_tuple[0])   # 'p' 
    print("Accessing tuple elements using indexing : ",my_tuple[5])   # 't'

    # nested tuple
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # nested index
    print("nested index: ",n_tuple[0][3])       # 's'
    print("nested index: ",n_tuple[1][1])       # 4

acesselementindex()
