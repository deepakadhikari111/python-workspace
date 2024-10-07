# Conditional statement will check the statement is true or not
# To check the condition we use if else

# WAP to check user eligible for voting
userAge = int(input("Enter your age"))
# Note the default input function return
# for vote user age must be greater than 18
if userAge > 18:
    print("you are eligible for voting")
else:
    print("you are not eligible")

# To check the user can sit in the first compartment in metro
usergender = input("Enter your gender")
# To check user is male or female
if usergender == "male":
    print("you can't sit in first compartment")
elif usergender == "female":
     print("you can sit in the first apartment")
else:
    print("you can sit in any compartment") 

# WAP if gender is female and age is greater than 18 -> get job easily
# else male age greater than 18 -> private job only 12
if userAge > 18:
    if usergender == "male":
       print("you can apply for private job")
    elif usergender == "female":
        print("you can apply for govt job") 
    else:
        print("sry there is no opening")
else:
    print("you'r under age")             

  

  