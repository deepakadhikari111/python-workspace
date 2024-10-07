# List can store different data, data can be different type int str
# List can store the duplicate data
# List is an ordered data set - string ascending descending

# Create list and store your friend name
friendlist = ["abhishek","chetan","rishab"]

# print the list of friend name
print(friendlist)

# Add the age of your friend into list
# Append will add the data into end of the list
friendlist.append(36) 
friendlist.append(22)
friendlist.append(33)
print(friendlist)  

# Add the data into list using index no
friendlist.insert(2,"deepak")
print(friendlist)

# To access the data using index no
print(friendlist[2])

# To delete data from list
friendlist.remove("abhishek")
print(friendlist)

# Pop will delete the data using index
friendlist.pop(3)
print(friendlist)

# Access the complete list
# for name in friendlist:
#     print(name)

friendlist.sort()

# Add the fav city name in list 
# Add my fav city nanital in first index 0
# Remove the last city in list
# Sorting the list data
# Print the list data 

favcity = ["manali","nanital","goa","pune","assam"]
favcity.insert(0,"nanital")
favcity.pop()
favcity.sort()
print(favcity)


