def loopuppercase():
    msg = input("Enter strings with uppercase in it : ")
    for i in msg:
        if i.isupper():
            print(i,end=".")


loopuppercase()
