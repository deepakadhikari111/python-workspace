# list in python
# list store multiple data
mylist = ["pawan","ivan","deepanshu"]
# tuple store multiple data
myTuple = ("pawan","ivan","deepanshu")
# set store multiple data
mySet = {"pawan","ivan","deepanshu"}
# dictionary store multiple data ina key value pair
myDict = {"name":"pawan","email":"p@gmail.com"}

# to check the data type of all above set
print("list:",type(mylist),"tuple",type(myTuple))
print("set:",type(mySet),"dict:",type(myDict))

# how to identify list,set,tuple,dictionary
# list -> [], tuple -> () , set -> {} , dict -> (:)

# example of data set
mydata = {"pawan","ivan","deepanshu","pawan"}
mygroup = ("pawan","ivan","deepanshu","pawan")
myclass = ["pawan","ivan","deepanshu","pawan"]
myfriends = ("pawan","ivan","deepanshu","pawan")
myDict = {"name":"pawan","age":33,"name":"pawan"}

# Access data from data set
print("list:",mylist[0])
print("tuple:",myTuple[0],"dict :",myDict["name"])

# Access complete data from data set
for data in mylist:
    print("list",data)
for item in mySet:
    print("set",item)
for value in myTuple:
    print("tuple",value)
for x in myDict.values():
    print("dict",x)  

# To check which data set support duplicate data
mylist[0] = "deepak"
print(mylist)
myDict["name"] = "deepak"
print(myDict)
# mySet[0] = "deepak"
# print(mySet)
# myTuple[0] = "deepak"
# print(myTuple)
#tuple,set is unchangeable
#list,set is changeable
#list,tuple duplicate item
#set,dict no duplicate item

# Add new value in data set
mylist.append("aditya")
mySet.add("aditya")
myDict.update({"name":"aditya"})
print("list",mylist,"tuple",myTuple,"dict",myDict,"set",mySet)

# To remove the data from the data set
myDict.pop("name")
mylist.pop(0)
mySet.remove("pawan")
print("list",mylist,"tuple",myTuple,"dict",myDict,"set",mySet)

# Convert tuple to list
convertlist = list(myTuple)
print(type(convertlist))

convertlist.append("rohan")
convertlist.pop(2)
print(convertlist)
myTuple = tuple(convertlist)
print(myTuple)