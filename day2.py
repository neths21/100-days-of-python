print("Welcome to the tip calculator!")
a=eval(input("What was the toal bill? $"))
b=int(input("How much top would you like to give? 10, 12, or 15?"))
c=int(input("How many people to spplit the bill?"))
d=(a/c)*((100+b)/100)
print("Each person should pay %0.2f"%d)