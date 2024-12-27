print("This program will give you how much income tax you need to pay")
print(""" For the First $10,000 interest is 0
 For the Second $10,000 interest is 10%
 For the remaining interest is 20%""")

Salary = int(input("Enter your Salary here: $ "))
Tax = 0

if Salary <= 10000:
    print("You don't have to pay any tax because your salary is on 0% tax slab")
elif 10000 < Salary <= 20000:
    A = Salary - 10000
    Tax = A*(10/100)
    print(f"The amount of tax you need to pay is $ '{Tax}' because your salary is on 10% tax slab")
    print(f"Here is the split of your salary $ {Salary} = $ 10,000*0% + $ {A}*10% = Tax Amount $ '{Tax}'")
else:
    B = Salary - 20000
    Tax = 10000*(10/100) + B*(20/100)
    print(f"The amount of tax you need to pay is $ '{Tax}' because your salary is on 20% tax slab")
    print(f"Here is the split of your salary $ {Salary} = $ 10,000*0% + $ 10,000*10% + $ {B}*20% = Tax Amount $ '{Tax}'")
