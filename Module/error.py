# Error handling in Python is the process of managing errors (also called exceptions) so your program doesn’t crash unexpectedly. Instead of stopping the entire program, Python lets you detect errors and respond properly.

# Why Error Handling Matters

# Without error handling:

# num = int(input("Enter a number: "))
# print(10 / num)

# If the user enters 0 or text like "hello", the program crashes.

# With error handling, the program can handle the problem gracefully.

# Basic Structure of Error Handling

# Python uses:

# try:
#     # code that may cause error
# except:
#     # code that runs if error happens

# Example:

# try:
#     num = int(input("Enter a number: "))
#     result=10 / num
#     print(result)
# except:
#     print("Only input a number")
# else:
#     print(f'THIS IS YOUR ANSWER{result}')


# How It Works
# Python tries to run the code inside try
# If no error occurs → program continues normally
# If an error occurs → Python jumps to except
# Handling Specific Errors

# Different errors exist in Python.

# Common ones:

# Error Type	Meaning
# ValueError	Wrong value type
# ZeroDivisionError	Division by zero
# TypeError	Wrong data type operation
# IndexError	Invalid list index
# KeyError	Missing dictionary key
# FileNotFoundError	File doesn’t exist

# Example:

# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# Now Python gives different messages depending on the problem.

# Using else

# else runs only if no error occurs.

# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result is", result)


# Using finally

# finally always runs whether there is an error or not.

# Useful for:

# Closing files
# Closing database connections
# Cleaning resources

# Example:

# try:
#     file = open("data.txt")

# except FileNotFoundError:
#     print("File not found")

# finally:
#     print("Execution finished")



# Full Structure
# try:
#     # risky code

# except SomeError:
#     # handle error

# else:
#     # runs if no error

# finally:
#     # always runs
# Getting the Actual Error Message

# You can store the error in a variable:

# try:
#     num = int(input("Enter number: "))

# except ValueError as e:
#     print("Error:", e)

# If user enters "abc":

# Error: invalid literal for int()


# Raising Your Own Errors

# You can create custom errors using raise.

# Example:

# age = -5

# if age < 0:
#     raise ValueError("Age cannot be negative")


# Custom Exception Example
# Exception
# class InvalidPasswordError(Exception):
#     pass

# password = "1235555"

# if len(password) < 6:
#     raise InvalidPasswordError("Password too short")
# Real-Life Example: Login System
# def login():
#     try:
#         email = input("Email: ")
#         password = input("Password: ")

#         if email != "admin@gmail.com":
#             raise ValueError("Invalid email")

#         if password != "1234":
#             raise ValueError("Wrong password")

#         print("Login successful")

#     except ValueError as e:
#         print(e)

# login()
# Best Practices

# Catch specific exceptions
# Keep try blocks small
# Use meaningful error messages
# Use finally for cleanup
# Avoid empty except blocks

# Bad practice:

# except:
#     pass

# This hides errors and makes debugging difficult.

# Common Exception Flow
# try:
#     x = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# finally:
#     print("Done")

# Output:

# Cannot divide by zero
# Done
# Summary

# Python error handling mainly uses:

# try → test risky code
# except → handle errors
# else → run if no error
# finally → always run
# raise → create errors manually

# It helps make programs:

# safer
# cleaner
# more professional
# user-friendly


















# ====================================Types of error ====================
# # 1. Basic `try-except`

# Handles any error generally.

# ```python
# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except:
#     print("An error occurred")
# ```

# ---

# # 2. Handling Specific Exceptions

# ## `ValueError`

# Occurs when wrong value type is used.

# ```python
# try:
#     age = int(input("Enter age: "))

# except ValueError:
#     print("Please enter a valid number")
# ```

# ---

# ## `ZeroDivisionError`

# Occurs when dividing by zero.

# ```python
# try:
#     result = 10 / 0

# except ZeroDivisionError:
#     print("You cannot divide by zero")
# ```

# ---

# ## `TypeError`

# Occurs when incompatible data types are used together.

# ```python
# try:
#     result = "10" + 5

# except TypeError:
#     print("Cannot add string and integer")
# ```

# ---

# ## `IndexError`

# Occurs when accessing invalid list index.

# ```python
# try:
#     names = ["John", "Mary"]
#     print(names[5])

# except IndexError:
#     print("Index does not exist")
# ```

# ---

# ## `KeyError`

# Occurs when dictionary key is missing.

# ```python
# try:
#     student = {
#         "name": "James"
#     }

#     print(student["age"])

# except KeyError:
#     print("Key not found")
# ```

# ---

# ## `FileNotFoundError`

# Occurs when file does not exist.

# ```python
# try:
#     file = open("data.txt", "r")

# except FileNotFoundError:
#     print("File does not exist")
# ```

# ---

# # 3. Multiple Exceptions

# Handling different errors separately.

# ```python
# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ValueError:
#     print("Invalid input")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# ```

# ---

# # 4. Multiple Exceptions in One Block

# ```python
# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except (ValueError, ZeroDivisionError):
#     print("Invalid operation")
# ```

# ---

# # 5. Using `else`

# Runs only if no error occurs.

# ```python
# try:
#     num = int(input("Enter number: "))
#     result = 100 / num

# except ZeroDivisionError:
#     print("Division by zero error")

# else:
#     print("Result =", result)
# ```

# ---

# # 6. Using `finally`

# Runs whether error occurs or not.

# ```python
# try:
#     file = open("sample.txt", "r")

# except FileNotFoundError:
#     print("File missing")

# finally:
#     print("Execution completed")
# ```

# ---

# # 7. Full Error Handling Structure

# ```python
# try:
#     num = int(input("Enter number: "))
#     result = 50 / num

# except ValueError:
#     print("Enter valid number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program ended")
# ```

# ---

# # 8. Getting Actual Error Message

# Using `as e`

# ```python
# try:
#     number = int("hello")

# except ValueError as e:
#     print("Error:", e)
# ```

# ---

# # 9. Raising Exceptions Manually (`raise`)

# ```python
# age = -2

# if age < 0:
#     raise ValueError("Age cannot be negative")
# ```

# ---

# # 10. Custom Exception

# Creating your own error type.

# ```python
# class InvalidAmountError(Exception):
#     pass


# amount = -500

# if amount < 0:
#     raise InvalidAmountError("Amount cannot be negative")
# ```

# ---

# # 11. Catching Custom Exception

# ```python
# class WeakPasswordError(Exception):
#     pass


# try:
#     password = input("Enter password: ")

#     if len(password) < 6:
#         raise WeakPasswordError("Password too short")

#     print("Password accepted")

# except WeakPasswordError as e:
#     print(e)
# ```

# ---

# # 12. Nested Try-Except

# ```python
# try:
#     try:
#         num = int(input("Enter number: "))
#         print(10 / num)

#     except ZeroDivisionError:
#         print("Inner: Cannot divide by zero")

# except ValueError:
#     print("Outer: Invalid input")
# ```

# ---

# # 13. Exception with User Login Example

# ```python
# users = [
#     {
#         "email": "admin@gmail.com",
#         "password": "1234"
#     }
# ]

# try:
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     found = False

#     for user in users:
#         if user["email"] == email and user["password"] == password:
#             found = True
#             print("Login successful")

#     if not found:
#         raise ValueError("Invalid login details")

# except ValueError as e:
#     print(e)
# ```

# ---

# # 14. Assertion Error

# ```python
# x = -5

# assert x > 0, "x must be positive"
# ```

# ---

# # 15. Import Error

# ```python
# try:
#     import abcxyz

# except ImportError:
#     print("Module not found")
# ```

# ---

# # 16. Attribute Error

# ```python
# try:
#     name = "James"
#     name.append("A")

# except AttributeError:
#     print("String has no append method")
# ```

# ---

# # 17. Name Error

# ```python
# try:
#     print(age)

# except NameError:
#     print("Variable does not exist")
# ```

# ---

# # 18. Overflow Error

# ```python
# import math

# try:
#     print(math.exp(1000))

# except OverflowError:
#     print("Number too large")
# ```

# ---

# # 19. Runtime Error

# ```python
# try:
#     raise RuntimeError("Something bad happened")

# except RuntimeError as e:
#     print(e)
# ```

# ---

# # 20. Keyboard Interrupt

# Occurs when user presses `CTRL + C`

# ```python
# try:
#     while True:
#         print("Running...")

# except KeyboardInterrupt:
#     print("Program stopped by user")
# ```

# ---

# # 21. Catching All Exceptions Safely

# ```python
# try:
#     num = int(input("Enter number: "))
#     print(10 / num)

# except Exception as e:
#     print("Error:", e)
# ```

# ---

# # 22. Best Practice Example

# ```python
# def divide_numbers():
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))

#         result = num1 / num2

#     except ValueError:
#         print("Please enter valid integers")

#     except ZeroDivisionError:
#         print("Cannot divide by zero")

#     else:
#         print("Answer =", result)

#     finally:
#         print("Calculation finished")


# divide_numbers()
# ```
