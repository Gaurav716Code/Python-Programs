def createfile():
    file1 = open("Test creation.txt", 'w')
    file1.write("F113 Gaurav Viskwakarma")
    print("File created")
    file1.close()

createfile()
