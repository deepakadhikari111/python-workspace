# WAP to print this pattern 1 3 7 11 13 15 using for loop  
for b in range(1,16,2):
    if b==9 or b==5:
        continue # skip the current iteration
    else:
        print(b)  