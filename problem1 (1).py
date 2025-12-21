# ==============================================================================
# LAB TASK SOLUTIONS - Python Programming Language – Basic Exercises
# ==============================================================================

# --- 1. Data Types and Variables ---
print("--- SECTION 1: Data Types and Variables ---")

# 1. Perform addition and concatenation using integers and strings separately
a = 10
b = 20
sum_result = a + b
print("Addition of integers:", sum_result)

str1 = "Hello"
str2 = "World"
concat_result = str1 + " " + str2
print("Concatenation of strings:", concat_result)

# 2. Check the type of a variable using type(), if float then convert to int and print both
num = 12.75
print("Type before conversion:", type(num))

if type(num) == float:
    num_int = int(num)
    print("Converted to integer:", num_int)
    print("Type after conversion:", type(num_int))

# 3. Create and print an f-string
name = "Alice"
age = 22
print(f"My name is {name} and I am {age} years old.")


# --- 2. Abstract Data Types (ADT) ---
print("\n--- SECTION 2: Abstract Data Types (ADT) ---")

# 1. Perform addition and concatenation using integers and strings separately
a = 10
b = 20
sum_result = a + b
print("Addition of integers:", sum_result)

str1 = "Hello"
str2 = "World"
concat_result = str1 + " " + str2
print("Concatenation of strings:", concat_result)

# 2. Check the type of a variable using type(), if float then convert to int and print both
num = 12.75
print("Type before conversion:", type(num))

if type(num) == float:
    num_int = int(num)
    print("Converted to integer:", num_int)
    print("Type after conversion:", type(num_int))

# 3. Create and print an f-string
name = "Alice"
age = 22
print(f"My name is {name} and I am {age} years old.")


# --- 3. Operators and Expressions ---
print("\n--- SECTION 3: Operators and Expressions ---")

# 1. Take two numbers as input and print sum, subtraction, multiplication, and division
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2. Check relational operators
print("\nRelational Operator Results:")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# 3. Use logical operators (and, or, not) to combine conditions
print("\nLogical Operator Results:")
print("(a > b) and (a > 0):", (a > b) and (a > 0))
print("(a < b) or (b < 0):", (a < b) or (b < 0))
print("not(a == b):", not (a == b))

# Task 4: Evaluate an expression using mixed operators.
# Prediction (PEMDAS/BODMAS):
# 1. 5 * 3 = 15
# 2. 10 / 2 = 5.0
# 3. 20 + 15 - 5.0 = 30.0
mixed_expression = 20 + 5 * 3 - 10 / 2
print(f"14. Mixed Expression (20 + 5 * 3 - 10 / 2) result: {mixed_expression}")



# --- 4. Conditional Statements ---
print("\n--- SECTION 4: Conditional Statements ---")

# 1. Check if a number is positive or negative
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Check if a number is even or odd
n = int(input("\nEnter an integer: "))
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. Find the largest of two numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("The largest number is:", a)
elif b > a:
    print("The largest number is:", b)
else:
    print("Both numbers are equal.")

# 4. Grade a score using if-elif-else
score = int(input("\nEnter your score (0–100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 5. Check if a year is a leap year or not
year = int(input("\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")




# --- 5. Iteration ---
print("\n--- SECTION 5: Iteration ---")

# 1. Use a for loop to print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# 2. Use range(start, stop, step) to print even numbers from 2 to 20
print("\nEven numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)

# 3. Use a while loop to calculate the sum of first 10 natural numbers
print("\nSum of first 10 natural numbers:")
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum =", total)

# 4. Use break to stop a loop when number = 5
print("\nUsing break (stop when number = 5):")
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 5. Use continue to skip printing number = 3
print("\nUsing continue (skip number = 3):")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)



# 1. Function that returns the sum of two numbers
def add(a, b):
    return a + b

print("Sum of 10 and 5 is:", add(10, 5))

