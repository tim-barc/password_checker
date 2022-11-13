import re

pattern = "[A-Za-z0-9@#$%^&+=]{12,}" 
pwd = input("Please enter a password to check: ")

print("") # adding a line break

try:
    with open("rockyou.txt", "rt") as f:
        for line in f:
            if pwd in line:
                print("Password found in rockyou wordlist\nmaking it vulnerable to credential stuffing attacks\n")
                break
except:
    if re.fullmatch(pattern, pwd):
        print("Your password appears to be secure!")
    else:
        print("Your password is weak!")
