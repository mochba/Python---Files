"""We really do not want to have to edit our Python code every time we want to 
process a different file. It would be more usable to ask the user to enter the file 
name string each time the program runs so they can use our program on different files 
without changing the Python code."""

try:  
    fhand = open(input("\nEnter the file name:"))
    count = 0
    for eachline in fhand:
        if eachline.startswith("Subject:"):
        # print(eachline)
            count = count + 1
    print("\n\nThere were {} line start with Subject: in the file {}" .format(count,fhand), "\n")
except:
    print("\nEnter a valid file name!!!!")
    quit()