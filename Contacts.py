# Contacts.py
# Welcome & askes user what they want to do
 
print("Welcome to contacts")
print("What would you like to do")
print("(1)Add a phone number")
print("(2)Print the full list of contacts")
print("(3)Enter name to retrieve contacts phone number")
print("(0)Exit the Contacts App")
choice = raw_input()
 
# the dictionary
phoneBook = {}
 
# a while statement to repeat each time the process
while choice !="0":
# if statement used if user wants to add a contact
        if choice =="1":
                print("Enter contact name")
                name = raw_input()
                print("Enter number for contact")
                number = raw_input()
                phoneBook[name] =  number
                print("1, 2, 3, 0")
                choice = raw_input()
 
# if user wants to print all the list in contact
        elif choice =="2":
                print(phoneBook)
                print("1, 2, 3, 0")
                choice = raw_input()
  
# user wants to look up for the number they can do that by looking up for the name                                    
        elif choice =="3":
                print("Enter name to retrieve contacts phone number")
                contactName = raw_input()
                print(phoneBook[contactName])
                print("1, 2, 3, 0")
                choice = raw_input()
 
# leaving the app
print("Thank you for using the app")
 
 