# Error
# print(x)

# Error handling
try:
   print(x)
except NameError:
    print("'x'is not defined") 
# Error 2
#y = 1/0
try:
    y=1/0
except ZeroDivisionError:
    print("divide by zero error")

# Error 3
name = "pawan"
#no = int(name)
try:
    no = int(name)
except ValueError:
    print("string can't convert into integer")

# Error 4
friends = ["ivan","anshu","wani"]
#friends[4]  
try:
    friends[4]
except IndexError:
    print("you are calling wrong index")

# Error 5
amount = 500
email = "p@gmail.com"
#total = amount + email
try:
    total = amount + email
except TypeError:
    print("can't be concatinate")