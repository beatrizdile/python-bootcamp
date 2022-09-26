#### Opening a text file, reading and printing it.# # file = open("my_file.txt"# 
# contents = file.read# 
# print(conten# )
# file.close()

### The 'with' will only open the file as long as we need it.
### we need to change the mode to be able to write on the file.
# with open("my_file.txt", mode="a") as file:
#     file.write("\nHello.")


### If you want to open a file that doesn't exist it's going to create it for you
# with open("other_new_file.txt", mode="a") as file:
#     file.write("hi")



