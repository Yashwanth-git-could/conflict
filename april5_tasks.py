# Password Validation
import re
password=input("Enter the Password: ")
pattern=r'^[A-Z][\w]*[@.-_$#%&*]+[\w]*$'
x=re.match(pattern,password)
if x:
    print("Valid Password")
else:
    print("Invalid Password")
    
# URL Validation
import re

url = input("Enter The URL: ")
pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+(\.[a-z]{2,})+$'

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")

# Exception handling
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print("Unexpected error")
else:
    print("Result:", c)
finally:
    print("Executed")

class NotEligible(Exception):
    pass
def checkage(age):
    if age<18:
        raise NotEligible("Age must be 18")
    else:
        print("eligible")
        
try:
    checkage(16)
except NotEligible:
    print("error",NotEligible)