recorded_speed=int(input("Enter the speed:"))
speed_limit=80
is_school_zone=bool(input("In School Zone? "))
excess_speed = recorded_speed - speed_limit
base_fine=50
demerit_point=2
court_summons="Mandatory court Summons"

if (excess_speed<=0):
    print("No violation")
    print(f"Recorded Speed{recorded_speed} Km/h")
    print(f"speed limit was {speed_limit} km/h")

elif(is_school_zone and excess_speed>0 ):
    print("$",2*base_fine,"Fine")
    print("School Zone",is_school_zone)
    print(f"Recorded Speed {recorded_speed} Km/h")
    print(f"speed limit was {speed_limit} Km/h")
elif(excess_speed>1 and excess_speed<15):
    print("$",base_fine,"Fine")
    print(f"Recorded Speed {recorded_speed} Km/h")
    print(f"speed limit was {speed_limit} km/h")

elif(excess_speed>16 and excess_speed<30):
    print("$",3*base_fine,"Fine" ,"and",demerit_point,"demerit point" )
    print(f"Recorded Speed {recorded_speed} Km/h")
    print(f"speed limit was {speed_limit} km/h")
elif(excess_speed>30):
    print("$",7*base_fine,"Fine", "and", 2*demerit_point,"demerit point","and", court_summons)
    print(f"Recorded Speed {recorded_speed} Km/h")
    print(f"speed limit was {speed_limit} km/h")


