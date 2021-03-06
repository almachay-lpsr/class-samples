# CS 6.5 Tools for Ciphers - Indpendent Practice
# Implement the functions below - when you've finished, all tests should pass
# Author: Alma Chay

# import statements here
import string


# calls function to create a list with the letters from a to z
# DOES NOT manually create the list
# use Google and/or Stack Overflow to find how to do this in python!
# returns a list with the lowercase letters a to z
def getLowercaseAlphabet():
	LowAlphabet = list(string.ascii_lowercase)
	return LowAlphabet

def getUppercaseAlphabet():
	upperAlphabet = list(string.ascii_uppercase)
	return upperAlphabet	

def getReorderedLowercaseAlphabet(key):
	letter= string.ascii_lowercase
	letterList = []
	count = 0 
	while count < 26:
		letterList.append(letter[(key + count) % 26])	
		count = count + 1
	return letterList


# DO NOT EDIT THE TESTS BELOW HERE!
# ------------
#

low_alpha = getLowercaseAlphabet()

try:

    if(low_alpha[5] == 'f' and low_alpha[9] == 'j'):
        print("Test 1 passes! getLowercaseAlphabet() is correct.")
    else:
        print("Test 1 fails. getLowercaseAlphabet() needs more work.")
except:
    print("Test 1 fails. getLowercaseAlphabet() needs more work.")



high_alpha = getUppercaseAlphabet()

try:
    if(high_alpha[7] == 'H' and high_alpha[11] == 'L'):
        print("Test 2 passes! getUppercaseAlphabet() is correct.")
    else:
        print("Test 2 fails. getUppercaseAlphabet() needs more work.")
except:
    print("Test 2 fails. getUppercaseAlphabet() needs more work.")

reorderAlphabet = getReorderedLowercaseAlphabet(5)

try:
    if(reorderAlphabet[5]) == 'k':
        print("Test 3 passes! getReorderedLowercaseAlphabet() is correct.")
    else:
        print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")
except: 
    print("Test 3 fails. getReorderedLowercaseAlphabet() needs more work.")
