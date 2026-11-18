from math_tools import is_positive as check_positive,cube

cube_Check = cube(int(input("Enter the number: ")))
positive_check=check_positive(int(input("Enter the number: ")))
print(f"cube: {cube_Check}")
print(f"Check Positive or negative: {positive_check}")