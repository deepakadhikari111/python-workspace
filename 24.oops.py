#OOPS IN PYTHON 
#Object oriented programming structure
#CLASS- it os a container which collection variables, functions
#Example--> dep CLASS
# dep.fullname = "deepakadhikari"
# dep.age = 19
# dep.sleeping()
# dep.eating()
# dep.watching()
#CLASS syntax:
# class ClassName:
#     statement
# ex-
class ClassName:
    print("This is my class")
#creating a class
class Dep:
    age = 19
    fullName = "Deepak Adhikari"
    email = "deepak@gmail.com"
    def pocketmoney(this,amount):
     print("My pocketmoney is", amount)
#create class object
dep:Dep =Dep()
print(dep.fullName)
print(dep.age)
print(dep.email)
dep.pocketmoney(12000)