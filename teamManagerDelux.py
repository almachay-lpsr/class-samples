# teamManagerDelux
# the begining of the improved code
class Player(object):

# def is  function that we will use later
# 5 things we will need to ask the manager of this team for the player
        def __init__(self, name, age, goals, jersey_num, position):
                self.name = name
                self.age = age
                self.goals = goals
 		self.jersey_num = jersey_num
		self.position = position

# in order for this to work we will have to have a special code to define each thing
        def printStats(self):
                print("name: " + self.name)
                print("age: " + self.age)
                print("goals: " + self.goals)
 		print("jersey_num: " + self.jersey_num)
		print("position: " + self.position)

# to save the team they have created 
# takes the playerList and the user's desired filename
# writes each Player to file
def saveTeam(nList, filename):
# open the file write to the file
	file = open(filename, "a")
# write to the file
	for p in nList:
		file.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(jersey_num) + " " + p.position + '\n')
# close the file
	file.close()

# takes a filename for a file of players 
#returns a list of Players
def loadTeam(filename):
# empty list
	list = []
	
# open  file
	file = open((filename), "r") 
	time = file.readline()
# read each line and create Player from it
	while time != "":
		time.split()
		letter = time.split()
		list.append(Player(letter[0], letter[1], letter[2], letter[3], letter[4])) 
# read each line and create Player and split variables
		time = file.readline()
# close file
	file.close()
# return ist
	return list


# the user will choose what they want to do
print("Enter the number of your choice")
print("(1) Start a new Team") 
print("(2) Open the file for existing team")
# enter the response 
answer  = raw_input()

# blank list
if answer == "2":
	print("What's the filename of exsiting team & enter name with .tmd extension")
	filename = raw_input()
	list = loadTeam(filename)
else:
	list = []
	
# this are the 3 things you can do and enter the letter
print("Choose what you would like to do") 
print("(a) Would you like to add player?") 
print("(b) Show the list of player") 
print("(c) Exit and save your data") 
# the response
choice = raw_input()

# a while statement that if user doesn't choose c then this will happen
while choice != "c":
# if user chooses a then this happens
	if choice == "a":
		print("Enter your name")
		name = raw_input()
		print("Enter age")
		age = raw_input()        
		print("Enter number of goals")
		goals = raw_input() 
		print("What is your jersey number") 
		jersey_num = raw_input()		
		print("What position do you play")
		position = raw_input()
       		list.append(Player(name, age, goals, jersey_num, position))
		print("a, b, c ?")
		choice = raw_input()

# if user chooses b then it shows the list
	elif choice  == "b":
                for p in list:
                        print(" ")
                        p.printStats()
                        print(" ")
                print(" a, b or c?")
                choice  = raw_input()

# if user chooses c then they want to create a file
	elif choice == "c":
		print("Enter the name of the file you will add players to, Don't forget to add tmd estension" )
		filename = raw_input()
		saveTeam(list, filename)

# the final touv=ch og the game is leaving
print("Hope you had a wonderful time with this app")

