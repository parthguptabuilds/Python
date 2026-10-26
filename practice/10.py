password = "Delhi@2026"

has_len = len(password) >= 8
has_upper = False
has_digit = False
has_special = False

for c in password:
    if c >= 'A' and c <= 'Z':
        has_upper = True
    if c >= '0' and c <= '9':
        has_digit = True
    if not c.isalnum():
        has_special = True

count = 0
if has_len:
    count = count + 1
if has_upper:
    count = count + 1
if has_digit:
    count = count + 1
if has_special:
    count = count + 1

if count == 4:
    strength = "Strong"
elif count >= 2:
    strength = "Moderate"
else:
    strength = "Weak"

print("Strength:", strength)
print("Failed rules count:", 4 - count)