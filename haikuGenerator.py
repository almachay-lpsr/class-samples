# ask the user to write something for the first line# haikuGenerator.py the beginning of coding first line 
# welcomes the user
print("Welcome to the Haiku generator!")

# ask the user to write something for the first line
print("Provide the first line of your haiku:")
# the user choice
Choice1 = raw_input()

# ask the user for the second line 
print("Provide the second line of your haiku:")
# user choice
Choice2  = raw_input()

# the third line
print("Provide the third line of your haiku:")
# user answer
Choice3 = raw_input()

# ask the user to name the file
print("What name would you like on your file?")
# the title of the file
fileName  = raw_input()

# to open the file 
myFile = open(fileName, 'a')

# to have all the lines you wrote together
together = [Choice1 + Choice2 + Choice3]	

# to have the user answer in order and perfectly
for line in together:
	myFile.write(str(line) + '\n')

# this will show once you finish every step and if you would like to view your answer
print("Done! To view your haiku, type 'cat' and the name of your file at the command line")

# to finish the coding
myFile.close()
