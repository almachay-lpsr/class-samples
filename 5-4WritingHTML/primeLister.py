# the begining of the new code to list all the numbers that are prime
def primenumbers(myNum): 
	for n in range(2,myNum):
# this will be able to divide the number from all the numbers in range
                if (myNum % n) == 0:
# this will return weather the number is false or true
                        return False
        return True

# it makes a new file to add prime numbers
myFile = open("prime.txt", "w")
# to make sure the number is from 2- 10001 and it would be in the list
for n in range(2,10001):
	if primenumbers(int(n)):
		myFile.write(str(n) + "\n")

# in the end everything closes the code finishes
myFile.close()

