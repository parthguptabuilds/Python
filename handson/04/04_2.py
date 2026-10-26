recorded_speed = int(input("Enter the speed: "))
speed_limit = 80

# Clean boolean conversion for school zone input
is_school_zone = input("In School Zone? (True/False): ").strip().capitalize() == "True"

excess_speed = recorded_speed - speed_limit
base_fine = 50
demerit_point = 2
court_summons = "Mandatory court Summons"

# Initialize default values to prevent NameError
fine = 0
Demerit_point = 0
court = "None"

if excess_speed <= 0:
    print("No violation")
else:
    print("violation Exceed")
    
    if is_school_zone:
        fine = 2 * base_fine
    elif 1 <= excess_speed < 15:
        fine = base_fine
    elif 16 <= excess_speed < 30:
        fine = 3 * base_fine 
        Demerit_point = demerit_point
    elif excess_speed > 30:
        fine = 7 * base_fine
        Demerit_point = 2 * demerit_point
        court = court_summons

    print(f"Fine ${fine}")
    print(f"Demerit point {Demerit_point}")
    print(f"court summons {court}")