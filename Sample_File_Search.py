# fhand = open('/home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt')
# # file_read = fhand.read() read only each letter from the line
# count = 0
# for eachline in fhand:
#     # print each line from the file
#     print(eachline.rstrip()) 
#     count = count + 1
# print(count)

# Find the line with From: in the file 
# fhand = open('/home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt')
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     print(line)
#     count = count +1
# print("Number of lines start with From: ",count)

# Find the line with @uct.ac.za in the file 
try:
    fhand = open('/home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt')
    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.find('@uct.ac.za') == -1: continue
        print(line)
        count = count +1
    print("Number of Emails id with domin name (uct.ac.za) in this file are",count)
except:
    print("Enter a valid file name!!!!!!")
    quit