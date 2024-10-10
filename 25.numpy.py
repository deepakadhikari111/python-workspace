import numpy as np

# Create numpy array to store
# Friends name,edit

myFriends = np.array(["ivan       ","anshu","wani","anjani"])

print(myFriends)
print(type(myFriends))
myFriends[2]
print(myFriends[2])

for name in myFriends:
    print(name)

myFriends[0]="ivan sharma"
print(myFriends)
print(myFriends[0])
myFriends.sort()
print(myFriends)
# mydata = np.flip(myFriends)
# print(mydata)

y = 3
while y>= 0:
    print(myFriends[y])
    y = y - 1