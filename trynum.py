tynum = input("Enter a number")
try:
    inval = int(tynum)
except:
    inval = -1;
if inval > 0:
    print("Thats a number")
else:
    print("Thats not a Number")    