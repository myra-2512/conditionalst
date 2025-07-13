#Activity1
num=3
if num>0:
    print(num,"is a positive number.")

num=-1
if num<0:
    print(num,"is a negatve number.")

#Activity2
actual_cost=float(input("Enter the cost price of the item:"))
sale_amount=float(input("Enter the selling price:"))

if (sale_amount > actual_cost):
    amount=sale_amount-actual_cost
    print("Total profit is={0}".format(amount))

else:
    print("Loss incurred in the transaction.")
#Activity3
i=int(input("Enter a number:"))
if(i<15):
    print("i is smaller than 15")
    print("This is an if block")
else:
    print("i is greater than or equal to 15")
    print("This is an else block")
print("I am neither part of if block nor else block")
#Activity4
number=int(input("Enter a number:"))
print("The number given is:",number)

if number%2==0:
    print("The number is even")

else:
    print("The number is odd")
