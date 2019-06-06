#1.creation of storage container
instagramUserName ="auribaises"
johnsAge = 12
time = 7
#instgramUserName is a name of s6torage container
#2. Update operation in container
johnsage = 22
time = 4
#3.Delete the operation
#del instagramUserName
#4. Read Storage container
print(instagramUserName)
print(johnsage)
print (time)
#5.Explore Memory for containers
#id of storage container is known as Hash code
print(hex(id(instagramUserName)))
print(hex(id(johnsage)))
print(hex(id(time)))
#PS: When program will be executed,our program will have RAM associated with it
# instagramUserName ,johnsage and time are REFERENCE VARIABLES.
#Referehnce variables will contain the Hash code of the  Data