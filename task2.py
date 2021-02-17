#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

username = ""



while username != "admin":
    username = input("What is your username?")
    if username!= "admin":
        print(" Access Denied")

print("Correct! What is your Password?")


password = ""

while password != "12345":
    password = input("What is your Password?")
    if password!= "12345":
        print("Access Denied")

print("Access Granted, Welcome back Mr. Kupillas")