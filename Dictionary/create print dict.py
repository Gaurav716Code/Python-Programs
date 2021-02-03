#Program to create and print dictionary
def createDict():
    # empty dictionary
    my_dict1 = {}

    # dictionary with integer keys
    my_dict2 = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict3 = {'name': 'John', 1: [2, 4, 3]}

    # using dict()
    my_dict4 = dict({1:'apple', 2:'ball'})

    # from sequence having each item as a pair
    my_dict5 = dict([(1,'apple'), (2,'ball')])

    print("my_dict1 : ",my_dict1)
    print("my_dict2 : ",my_dict2)
    print("my_dict3 : ",my_dict3)
    print("my_dict4 : ",my_dict4)
    print("my_dict5 : ",my_dict5)

createDict()
