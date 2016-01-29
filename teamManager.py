# teamManager.py
# soccer team code

# begin the code for teamManager
class Player(object):

	def __init__(self, name, age, goals):
		self.name = name
		self.age = age
		self.goals = goals
	
	def printStats(self):
		print("name: " + self.name)
                print("age: " + self.age)
                print("goals: " + self.goals)

# asks if you want to add player,show the list or just leave
print("Choose what you would like to do")
print("(1) Would you like to add player?")
print("(2) Show the list of player")
print("(0) Exit and delete players")
answer = raw_input()
list = []

# a statement to go with user option for number 1
while  answer != "0":
	if answer == "1":
		print("write name")
		name = raw_input()
		print("write age")
		age = raw_input()
		print("write goals this person has done")
		goals = raw_input()
		list.append(Player(name, age, goals))
		print(" 1, 2 or 0?")
		answer = raw_input()
		
# the code for choice 2
	elif answer == "2":
		for p in list:
			print(" ")
			p.printStats()
			print(" ")
		print(" 1, 2 or 0?")
		answer = raw_input()

# answer choice for number 0
if answer == "0":
	print("Bye.")

# the ending for problem 
