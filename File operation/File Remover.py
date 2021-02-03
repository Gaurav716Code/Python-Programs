import os
if os.path.exists("Test creation.txt"):
    os.remove("Test creation.txt : File Deleted ")
else:
    print("File does not exist")
    
