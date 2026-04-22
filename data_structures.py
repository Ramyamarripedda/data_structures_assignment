'''Task 1 — Tuples Create a tuple of five city names, 
unpack it into five separate variables, and print each 
variable. Then try to modify the first element and handle 
the resulting error with a try-except block that prints a 
clear message.'''
# Create a tuple of five city names
city_names = ("hyderabad", "bangalore", "delhi", "mumbai", "chennai")
# Unpack the tuple into five separate variables
city1, city2, city3, city4, city5 = city_names
# Print each variable
print("city1:", city1)
print("city2:", city2)
print("city3:", city3)
print("city4:", city4)
print("city5:", city5)
# Try to modify the first element and handle the resulting error
try:
    city_names[0] = "kolkata"
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable, so their elements cannot be changed.")

'''Task 2 — Sets Create two sets — one for students
who passed a Python test and one for students who passed
a SQL test. Print the union, intersection, and difference
(Python-only passers) using set operators.'''

# Create two sets for students who passed Python and SQL tests
python_passers = {"Ramya", "Sita", "Priya", "pramod"}
sql_passers = {"Priya", "pramod", "pravasya", "pravasthi"}

# Print the union of the two sets
union_passers = python_passers | sql_passers
print("Union of Python and SQL passers:", union_passers)

# Print the intersection of the two sets
intersection_passers = python_passers & sql_passers
print("Intersection of Python and SQL passers:", intersection_passers)

# Print the difference (Python-only passers)
python_only_passers = python_passers - sql_passers
print("Python-only passers:", python_only_passers)

'''Task 3 — Lists and ASCII Create a list of five integers 
representing ASCII values. Use a loop with chr() to print 
each integer alongside its corresponding character. Then 
use ord() to retrieve and print the ASCII value of the 
character 'Z'.'''

# Create a list of five integers representing ASCII values
ascii_values = [65, 66, 67, 68, 69]

# Use a loop with chr() to print each integer alongside its corresponding character
print("ASCII values and their corresponding characters:")
for value in ascii_values:
    print(f"{value}: {chr(value)}")

# Use ord() to retrieve and print the ASCII value of the character 'Z'
ascii_value_Z = ord('Z')
print("ASCII value of 'Z':", ascii_value_Z)

'''Task 4 — Subprocess Use the subprocess module to run 
the shell command whoami and print the captured output 
using result.stdout.'''

import subprocess

# Use the subprocess module to run the shell command whoami
result = subprocess.run(['whoami'], capture_output=True, text=True)

# Print the captured output using result.stdout
print("Output of whoami command:", result.stdout.strip())


