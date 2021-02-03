def filereader():
    file1 = open("Test creation.txt", 'r')
    for x in file1:
        print(x)

    print("End of File")

filereader()
