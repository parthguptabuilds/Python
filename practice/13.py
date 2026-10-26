units = 250
is_late = True


if units>0 and units<=100: 
    charges= units*5
elif units>100 and units<200:
    charges= units*5
elif units>200:
    charges=10
if is_late:
    surcharge=charges+150

print(f"Total Units {units} Units")
print(f"base bill amount {charges} rupee") 
print(f"surcharge {surcharge} rupee") 