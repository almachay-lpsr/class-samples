# applyCipher.py
# A program to encrypy/decrypt user text using Caesar's Cipher
# 
# Author: rc.chayjocol.alma [at] leadsps.org

# makes a mapping of encoded alphabet to decode alphabet
# argument: key
# returns: dictionary of mappped letters
def createDictionary():
    
    # placeholder
    return{}


# gets the encrypted message from user
# argument: none
# returns: 

def getMessage():
    pass 
    
    
# for each letter in the message, decodes and records
# arguments: encoded message,dictionary
# returns: decoded message
def decodeMessage(message,dictionary):
    pass

# outputs the message to the terminal 
# arguments: decoded message 
# returns: none 
def printMessage(message):
    pass


# execution starts here 

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodeMessage = decodeMessage(encodedMessage,dictionary)

printMessage(decodedMessage)

