cart_total=float(input("Enter the price of total cart: "))
member_tier=input("Enter the Member Tier: ")
coupon=input("Enter the coupon: ")

if(member_tier=="standard"):
    discount=0
else:
    if(member_tier=="platinum"):    
        discount=0.20
    elif(member_tier=="gold"):
        discount=0.15
    elif(member_tier=="silver"):
        discount=0.10
        
if(coupon=="SUPER5"):
        additional=0.05
elif(coupon=="nill"):
     additional=0
    
if(cart_total>=50 or member_tier=="Gold" or member_tier=="Platinum"):
     shipping=0
else:
     shipping=9.99

amount= cart_total-discount+shipping-additional
print("--------------------------------------------------------------")
print(f"Member tier: {member_tier}")
print(f"Total Cart Amount: {cart_total}")
print(f"Discount Applied:-${discount}")
print(f"Shipping charges:+${shipping}")
print(f"Total Bill: ${amount}")