
age_in_string=input("Enter your age :")
age=int(age_in_string)

day="Wednesday"

price=12 if age >=18 else 8

if day =="Wednesday":
    price-=2

print("Ticket price for you is $",price)
