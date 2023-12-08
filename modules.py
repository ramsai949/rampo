### write a program to print a number of lines,wordsand characters present in the given file
# file = open("sample1.txt", "r")

# number_of_lines = 0
# number_of_words = 0
# number_of_characters = 0
# for line in file:
#   line = line.strip("\n")
# #won't count \n as character
# words = line.split()
# number_of_lines += 1
# number_of_words += len(words)
# number_of_characters += len(line)

# file.close()

# print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)



# ####### write a programto show the content of a file and if file not exist then tell the user
# file is not avaialable



# try:
#     # Input the file name from the user
#     file_name = input("Enter the file name: ")

#     # Try to open the file for reading
#     with open(file_name, 'r') as file:
#         # Read and print the content of the file
#         file_content = file.read()
#         print(f"Content of the file '{file_name}':\n{file_content}")
# except FileNotFoundError:
#     print(f"The file '{file_name}' is not available.")


### write a program for handling binary data for vedio file


# Input video file and output video file
# Input video file and output video file



# input_video_filename = "input_video.mp4"
# output_video_filename = "output_video.mp4"

# try:
#     # Open the input video file in binary read mode
#     with open(input_video_filename, "rb") as input_file:
#         # Read the binary data
#         video_data = input_file.read()

#         # Open the output video file in binary write mode
#         with open(output_video_filename, "wb") as output_file:
#             # Write the binary data to the output file
#             output_file.write(video_data)

#     print(f"Video data has been successfully copied from '{input_video_filename}' to '{output_video_filename}'.")

# except FileNotFoundError:
#     print("The input video file is not available.")
# except Exception as e:
#     print(f"An error occurred: {e}")




##### write a program through the handling of csv files



import csv

# Sample CSV data
# csv_data = [
#     ["Name", "Age", "City"],
#     ["John", 30, "New York"],
#     ["Alice", 25, "Los Angeles"],
#     ["Bob", 35, "Chicago"],
# ]

# #Write data to a CSV file
# with open("sample_data.csv", mode="w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(csv_data)

# print("Data has been written to sample_data.csv")

## Read data from the CSV file
# with open("sample_data.csv", mode="r") as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)

## Modify data and write to a new CSV file
# new_csv_data = csv_data.copy()
# new_csv_data[2][1] = 26  # Modifying Alice's age

# with open("modified_data.csv", mode="w", newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(new_csv_data)

##print("Modified data has been written to modified_data.csv")



###### write a program to read data fromcsv file


#import csv

## Specify the path to your CSV file
# csv_file_path = "sample_data.csv"

# try:
#     with open(csv_file_path, mode="r") as csv_file:
#         reader = csv.reader(csv_file)

        ## Iterate through each row in the CSV file
#         for row in reader:
#             print(row)
# except FileNotFoundError:
#     print(f"The CSV file '{csv_file_path}' is not available.")
# except Exception as e:
#     print(f"An error occurred: {e}")



######  


#1

#file = open("myfile.txt",'w')

#students = ['ram','sai','imran','chinnu','indu']
#marks = [85,90,75,70,95]
#htnumber = [123,234,456,567,678]

#for i in range(0,5):
#    entry = students[i] + "-" + str(marks[i])+'\n'
#    file.write(entry)
#    entry = students[i] + "-" + str(htnumber[i])+'\n'
#    file.write(entry)
    
#file.close()


#2 

# f = open("sai.txt",'w')
# n = int(f.readline())
# print("total number of students : ",n)
# for i in range(n):
#     print("student number : ",i+1,":",end="")
#     grade = (f.readline().split())
#     print(grade)
#     sum = 0
#     for j in range(len(grade)):
#         sum=sum+int(grade[j])
#         per = ((sum/500)*100)
#         print("total marks : ",sum)
#         print("percentage : ",per)
#         print("\n")


# To read the file and have to create the file

# f = open("syed.txt","r")
# print(f.read())   # print all lines
# print(f.readline(),end="") # print first line
# print(f.readline()) # print second line
# print(f.readline(8)) # It will print 8 chracters in first line

#------------------------------------------#

# To create the file, If it was not created

# f1 = open("abc","w")
# f1.write("Hello world") # it will not print in output, It will write in abc file
# f1.write("Cricket") # if you remove and write it we will lost the data

#--------------------------------------------------------------#
# To append the file to existing file that was gone to last 

# f1 = open("abc",'a')
# f1.write("Hyd")

# f1 = open("abc","a")
# f1.write("INDIA")

#---------------------------#

# To copy the data from one file to other file by using for loop

# f = open("syed.txt","r")
# f1 = open("abc","w")

# for i in f:
#     f1.write(i)






#1

#file = open("myfile.txt",'w')

#students = ['ram','sai','imran','chinnu','indu']
#marks = [85,90,75,70,95]
#htnumber = [123,234,456,567,678]

#for i in range(0,5):
#    entry = students[i] + "-" + str(marks[i])+'\n'
#    file.write(entry)
#    entry = students[i] + "-" + str(htnumber[i])+'\n'
#    file.write(entry)
    
#file.close()


#2 

# f = open("sai.txt",'w')
# n = int(f.readline())
# print("total number of students : ",n)
# for i in range(n):
#     print("student number : ",i+1,":",end="")
#     grade = (f.readline().split())
#     print(grade)
#     sum = 0
#     for j in range(len(grade)):
#         sum=sum+int(grade[j])
#         per = ((sum/500)*100)
#         print("total marks : ",sum)
#         print("percentage : ",per)
#         print("\n")
