day=input("Enter the day of the week:")
age=int(input("Enter your age:"))

price=0
if(day.lower()=="wednesday"):
    price=-2;

if(age<=18):
    price+=8
else:
    price+=12

print("The ticket price is $"+str(price)+" on the day "+day +" for age "+str(age))