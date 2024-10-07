# -> # is used to comment the lien
# -> it is used to define the code meaning
# -> it can also comment and uncomment multiple line using ctrl+/

# comments examplem
# write a program to print your name
print("my name is deepak adhikari") # print function is used to display statement

# variables can store the value and it can change at any time
name = "deepak adhikari"
# pass the variable in the print function
print("my name is "+name) # + is used to concatenate the strings

#declare and initialize the multiple variables
age = 33
gender = "male"
# pass the multiple variable in print function
# this line give the type error
# reason for error str can't be concatenate with integer
# problem
# print("my name is"+ name
#       "my age is "+ age + "and gender is "+gender)
# solution 1 - int variable + replace by ,
print(" my name is "+ name +
      " my age is ", age ," and gender is "+ gender)
# solution 2 - enclosed the variable inside string statement using f


print("")

# DATA TYPE
print(type(name)) # type function return datatype of variable
print(type(age))
#1 str -> it can store the string data e.g.name ="deepak adhikari"
#2 int -> it can store the numeric data e.g name="33"
#3 float-> it can store the decimal no e.g pecentagee="75.45"

#Typecasting in python :-convert one datatype to another datatypes
#e.g sometime when we purchase item in float we paid in integer

purchaseitemprice=90.32
paiditemprice=int (purchaseitemprice)
print("paid amount is",paiditemprice)



#  it is not possible string to int
# name="pawan"
# fname=int(name)
# print("name is",fname)

#but int to  string is possible
ageinstring=str(age)

print("my age  is " + ageinstring + " and gender is "+gender)