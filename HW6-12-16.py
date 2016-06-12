# applyCipher.py
# HW6-12-16.py
# A program to encrypt/decrypt user text using Caesar's Cipher
# Author: rc.chayjocol.alma [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters 
import string

# the begining of Dictionary
def createDictionary(key):
	low = list(string.ascii_lowercase)
	UPPER = list(string.ascii_uppercase)
	alphaDict = {}
	ct = 0
	for l in low:
 		alphaDict[l] = low[(key + ct) % 26]
 		ct = ct + 1
	for l in UPPER: 
 		alphaDict[l] = UPPER[(key + ct) % 26]
 		ct = ct + 1
 	return alphaDict 
 
# gets the encrypted message from the user 
# arguments: none 
# returns: encoded message
def getMessage(message):
	return message
 
# for each letter in message, decodes and records 
# arguments: encoded message, dictionary 
# returns: decoded message
def decodeMessage(message, dictionary):
	MSG = ""
	for m in message:
		acletter = dictionary[m]
		MSG = MSG + acletter 
	return MSG
	 
# outputs the decoded message to the terminal 
# arguments: decoded message 
# returns: none
def printMessage(decodedmessage):
	print(decodedmessage)

# begins the code
try:

    # ask the user for key
    print("What key would you like to decode?")
    key = int(raw_input())

    dictionary = createDictionary(key)
    
    # ask user for message to decode
    print("What message would you like to decode?")
    message = raw_input()

    # records message
    encodedMessage = message

    # decodes message
    decodeMessage = decodeMessage(encodedMessage, dictionary)
    print("Here's your decoding message:")
    printMessage(decodeMessage)
    
except:
    print("Sorry,code can't be accepted.")
