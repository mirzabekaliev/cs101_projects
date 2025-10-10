age = int(input("enter your age: "))
next_year = age + 1
print(f" your age:{age}")
print(f'next year you will be: {next_year}')

name = "Mirzabek"
surname = "Aliev"
age = 18
nex_year = int(age) + 1
print("My name is " + name + " and  I am "+ str(age) + "  years old.")
print(f" my name is {name} {surname} and I am {age} years old")
print (f'Next year I will be {next_year}')
print(f"next year i will be {age + 1} years old")

price = 15999.5
print(f"price: {price:.2f} sum")
pi = 3.141599265359
print(f" Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 5 decimals: {pi:.5f}")
print(int(pi) )
print(f"{pi}")

item = input(" Enter your item name bro: ")
quantity = int(input(" How much do you have?: "))
price_per_item= float(input("Enter your price bro: "))

total = quantity * price_per_item

print(f"\n{'='*40}")
print(f"        RECEIPT")
print(f"{'='*40}")
print(f'Item: {item}')
print(f"Quantity:{quantity}")
print(f"Price per item: {price_per_item:.2f} sum")
print(f"{'='*40}")
print()