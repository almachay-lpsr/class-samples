 
walking_file = open('walking_instructions.txt' , 'r')
 
lineToPrint = walking_file.readline() 
while lineToPrint != " ":
        print(lineToPrint + ", duh") 
lineToPrint = walking_file.readline()
 
walking_file.close()
