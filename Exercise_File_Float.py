"""Write a program to prompt for a file name, and then read through the file and look 
for lines of the form:"""

# /home/appu/Documents/python_workbench/Chuks_python/mbox-short.txt
float_value_list = list()

try:
    count = 0
    float_value = 0
    float_sum = 0
    fhand = open(input("Enter a file name :"))
    for eachline in fhand:
        if eachline.startswith("X-DSPAM-Confidence:"):
            print(eachline)
            float_list = eachline.split()
            float_value = float_list[1]
            float_value_list.append(float_value)
            count = count + 1
    print(float_value_list)
    val = 0.0
    for i in range(0,len(float_value_list)):
        value  =  float_value_list[i]
        fl_value = float(value)
        val  = float(val) + fl_value
    print("Sum of the above float list is ",val)
    print("Number of float values in this file are :",count)
    print("Average of the above folat list is :",val/count)
except:
    print("Enter a valid file!!!!")
    quit()


# Method 2 to slove the problem
# f_name = input("Enter a file name :")
# f_store = open(f_name)
# count = 0
# nf = 0
# for f_line in f_store:
#     if not f_line.startswith("X-DSPAM-Confidence:"): continue
#     else:
#         print(f_line.strip())
#         count = count + 1
#         n = f_line.find(":")
#         piece = f_line[n+1:]
#         f = piece.strip()
#         nf = nf + float(f)
# print("\nSum of the float value %s :" ,nf)
# print("Number of Lines in the file : " ,count)
# print("Average of the float value: " ,nf/count)
# print("Done")



