"""
Assignment-1:
WAP to print the following output using print function
1 2 3 4 5
"""
print("1 2 3 4 5")

"""
Assignment-2:
# WAP to print the following output using print function
1 2 3 => Same line, one space between each value
4    5 => Same line, tab space between each value

"""
print("1 2 3 \n4 \t5")
# OR
print("1", "2", "3", sep=" ")
print("4", "5", sep="\t")
"""
Assignment-3:
WAP to print 'Hi' on the screen
and 'I Love Python' to the file using the print function
"""
print(" Hi ")

f = open("text_file.txt","w")
print("I love Python",file=f)