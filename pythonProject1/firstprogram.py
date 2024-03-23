# write a program to create a billing system at supermarket.
while True:
    name=input("enter customer's name:")
    total=0;
    while True:
        print("enter the amount and quantity")
        amount=float(input("enter amount: "))
        quantity=float(input("enter quantity: "))
        total+=amount*quantity
        repeat=input('do you want to add more items? (yes/no): ')
        if repeat=="no" or repeat=="No":
            break
    print("-"*40)
    print("Name: ",name)
    print("amount to be paid: ",total)
    print("-"*40)
    print("****Happy Shopping****")

    repeat1=input("do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat1 == "No":
        break