"""Enter a file and convert eachline into a UPPPER and print all the lines in the 
specified file name"""

try:
    fhand = open(input("\nEnter the file name:"))
    count = 0
    for eachline in fhand:
        new = eachline.upper()
        count = count + 1
        print(new)
    print("\n\nThere were {} line in the file {}" .format(count,fhand), "\n")
except:
    print("Enter a valid file name!!!!!!")
    quit()