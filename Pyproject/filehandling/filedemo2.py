file = open("firstfile.txt","r")

print(str(file.read()))
file.close()

print("line by line  =====================>")

my_file_line = open("firstfile.txt","r")
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()

with open("withas.txt","w") as my_file_withas :
    my_file_withas.write("hello how are")

with open("withas.txt","r") as my_file_read_withas:
    print(str(my_file_read_withas.read()))


