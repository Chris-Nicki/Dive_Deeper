# 1. Decisions at the Crossroad
# Task 1.Code Correction

number = int(input("Enter a number"))

if number >= 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else: 
    print("The number is negative.")

# 2. the Greatest Showdown
# Task 1. Identify the Greatest

number_1 = int(input("Hello, give me a number:"))
number_2 = int(input("Give me another number:"))
number_3 = int(input("NEED ONE MORE NUMBER!:"))

if number_1 > number_2 and number_1 > number_3:
    print(f"{number_1} is the biggest number")
elif number_2 > number_1 and number_2 > number_3:
    print(f"{number_2} is the largest number")
else:
    print(f"{number_3} is the largest number")

# Task 2. Identify the Smallest

number_1 = int(input("Hello, give me a number:"))
number_2 = int(input("Give me another number:"))
number_3 = int(input("NEED ONE MORE NUMBER!:"))

if number_1 < number_2 and number_1 < number_3:
    print(f"{number_1} is the smallest number")
elif number_2 < number_1 and number_2 < number_3:
    print(f"{number_2} is the smallest number")
else:
    print(f"{number_3} is the smallest number")