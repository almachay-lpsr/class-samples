import random
 
random.randint(1,2)
 
print("(1) Would you like to write your haiku from scratch")
print("(2) Get a randomized first line?")
 
answer = raw_input()
 
if answer != "2":
        print("Provide the first line of your haiku:")
    
        Choice1 = raw_input()
 
        print("Provide the second line of your haiku:")
        Choice2 = raw_input()
 
        print("Provide the third line of your haiku:")
        Choice3 = raw_input()
 
        print("What name would you like on your file?")
        fileName = raw_input()
 
        myFile = open(fileName, 'a')
 
        together = [Choice1 + Choice2 + Choice3]
 
if answer == "2":
        print("here the first line")
        print("write your story till your out of words")
 
        print("write the second line")
        answer = raw_input()
 
	print("write the third line")
        name = raw_input()
	
 	print("write a name to you're file")
       	fileName = raw_input() 

myFile = open(fileName, 'a')
 
all = [answer + name]
 
for l in all:
         myFile.write(str(l) + '\n')
 
print("Done! To view your haiku, type 'cat' and the name of your file at the command line")
 
myFile.close()
 
