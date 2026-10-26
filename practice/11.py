password="Delhi@2026"
has_length = False
has_digit = False
has_upper = False
has_splchar = False

if len(password)>=8:
    has_length=True
    

for i in password:
    if i.isdigit():
        has_digit=True
    if i.isupper():
        has_upper=True
    if i in "!@#$%^&*":
        has_splchar=True

if has_length and has_digit and has_upper and has_splchar:
    pass_check="Strong"

elif has_length and has_digit and has_upper:
    pass_check="Moderate"

else:
    pass_check="Weak"

print(f"Password length check: {has_length}")
print(f"Password strength: {pass_check}")

