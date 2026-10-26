time=float(input("Enter the time:-"))

if(time>9.30 and time<10.30):
    print("Teacher is teaching the class")

elif(time<9.30 and time>9.00):
    print("Teacher is waiting for class to start!")
else:
    print("Class is over!")