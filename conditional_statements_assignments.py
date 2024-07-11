# Assignment-1: if condition
# Check if a person is eligible to vote based on their age

# Input: Age of the person

# Check if the person is eligible to vote

age = int(input("Please enter your AGE : "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative
num = int(input("Please enter a number :"))
if num < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is a positive number")

# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd

num1 = int(input("please enter a number :"))
if num1 % 2 == 0:
    print(f"{num1} is a even number")
else:
    print(f"{num1} is a odd number")

# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers
n1 = int(input("please enter 1st number :"))
n2 = int(input("please enter 2nd number :"))
n3 = int(input("please enter 3rd number :"))
if n1 > n2 and n1 > n3:
    print(f"{n1} is greatest.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greatest.")
else:
    print(f"{n3} is greatest.")
# Assignment-5: nested if else condition
"""
# 
# Movie Ticket Pricing
# Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:
# 
# Regular price: $10
# Children under 12 and seniors over 65 get a 50% discount.
# Matinee show (before 5 PM) offers a 25% discount to all.
# """
actual_ticket_price = 10.0
ticket_price_to_pay = 10.0
customer_age = int(input("please enter age for movie ticket: "))
time = float(input('please enter on what time you want to book ticket :'))
if time < 17.00 and (customer_age < 12 or customer_age > 65):
    ticket_price_to_pay = ticket_price_to_pay - (actual_ticket_price / 4)
    ticket_price_to_pay = ticket_price_to_pay - (actual_ticket_price / 2)
elif 65 < customer_age < 12:
    ticket_price_to_pay = ticket_price_to_pay - (actual_ticket_price / 2)
elif time < 17.00:
    ticket_price_to_pay = ticket_price_to_pay - (actual_ticket_price / 4)

print(f"total price to pay ={ticket_price_to_pay}rs")

# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population

country_1 = int(input("Enter the population of country_1: "))
country_2 = int(input("Enter the population of country_2: "))
country_3 = int(input("Enter the population of country_3: "))
if country_2 > country_3 and country_2 > country_1:
    print("country_2 has largest population.")
elif country_1 > country_3 and country_1 > country_2:
    print("country_1 has largest population.")
else:
    print("country_3 has largest population.")
