# Create file for saving laptop password
# Open function will create a file
# When file is not exists and write the file
myPassword = open("password.txt","w")

# Write my laptop password in file
myPassword.write("my laptop password - ghuighui")

# Overwrite the new password using userinput
myPassword.write(input("enter new password"))

# Read the password from file
myPassword = open("password.txt","r")
mydata = myPassword.read()
if "lap" in mydata:
    print("yes")
else:
    print("no")

# To close file    
myPassword.close()

# delete the file
import os
os.remove("password.txt")

# Create read write delete csv,excel,json,txt
# Create csv file
myCsv = open("myfile.csv","w")
myCsv.write("pawan,dev,sanjay,mukesh,jay")

myexcel = open("myexcel.xlsx","w")
myexcel.write("name,pawan,dev,sanjay,mukesh,jay")

