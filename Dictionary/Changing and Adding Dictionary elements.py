#Changing and Adding Dictionary elements
def changeAddValue():
    # Changing and adding Dictionary Elements
    my_dict = {'name': 'Jack', 'age': 26}

    #Output: {'age': 26, 'name': 'Jack'}
    print(my_dict)

    # update value
    my_dict['age'] = 27

    #Output: {'age': 27, 'name': 'Jack'}
    print(my_dict)

    # add item
    my_dict['address'] = 'Downtown'

    # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    print(my_dict)
    
    # add item using update()  
    my_dict.update({"mobile": 982000000})

    # Output: {'name': 'Jack', 'age': 27, 'address': 'Downtown', 'mobile': 982000000}
    print(my_dict)

changeAddValue()
