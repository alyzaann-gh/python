fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

if fnum > snum:
    print(""+str(fnum)+" is greater than "+str(snum)+".")
elif fnum < snum:
    print(""+str(fnum)+" is less than "+str(snum)+".")
else:
    print(""+str(fnum)+" is equal to "+str(snum)+".")