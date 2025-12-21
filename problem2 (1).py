#Tasks 1:
# 1
a = 10
b = 5
print("Addition:", a + b)

x = "Hello"
y = "World"
print("Concatenation:", x + " " + y)

# 2
num = 12.7
print("Type before conversion:", type(num))
num_int = int(num)
print("Converted to int:", num_int)
print("Type after conversion:", type(num_int))

# 3.
name = "Alice"
age = 22
print(f"My name is {name} and I am {age} years old.")






#Tasks 2: 
# 1. List
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print("Updated List:", numbers)

# 2. Tuple
names = ("Zihan", "Aisha", "Rafi")
print("Second name in tuple:", names[1])

# 3. Dictionary
student = {"name": "Zihan", "id": 22, "gpa": 3.85}
print("Keys:", student.keys())
print("Values:", student.values())

# 4. Set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)

# 5
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(dup_list)
print("After removing duplicates:", unique_set)

#Tasks 3: 
# 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2
print("a > b:", a > b)
print("a == b:", a == b)
print("a < b:", a < b)

# 3
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > b):", not(a > b))

# 4
expr = a + b * 2 - 5 / 2
print("Expression result:", expr)




#Task  4:
# 1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Negative")

# 2.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

# 4
score = int(input("Enter score: "))
if score >= 80:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 40:
    print("Grade: C")
else:
    print("Grade: F")

# 5
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


#Tasks 5: 
# 1
for i in range(1, 11):
    print(i)

# 2
for i in range(2, 21, 2):
    print(i)

# 3
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum of first 10 natural numbers:", total)


# 4
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 5
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

