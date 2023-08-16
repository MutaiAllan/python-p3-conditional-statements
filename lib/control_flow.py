#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN":
        if password == "12345":
            return("Access granted")
        else:
            return("Access denied")
    else:
        return("Access denied")

def hows_the_weather(temperature):
    if temperature < 40:
        return("It's brisk out there!")
    elif temperature > 40 and temperature < 60:
        return("It's a little chilly out there!")
    elif temperature > 85:
        return("It's too dang hot out there!")
    else:
        return("It's perfect out there!")

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return("FizzBuzz")
    elif num % 5 == 0:
        return("Buzz")
    elif num % 3 == 0:
        return("Fizz")
    else:
        return(num)

def calculator(operation, num1, num2):
    if operation == '+':
        return (num1 + num2)
    elif operation == '-':
        return (num1 - num2)
    elif operation == '*':
        return (num1 * num2)
    elif operation == '/':
        return (num1 / num2)
    else:
        print("Invalid operation!")
        return None

print(admin_login("sudo", "12345"))
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))
print(hows_the_weather(33))
print(hows_the_weather(99))
print(hows_the_weather(75))

print(fizzbuzz(1))
print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(15))

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 4, 4))
print(calculator("/", 4, 2))
print(calculator("nope", 1, 1))