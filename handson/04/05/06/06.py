entered_pin=input("Enter the pin: ")
actual_pin="1234"
account_balance=float(input("Enter the Balance: "))
requested_amount=float(input("Enter the Amount: "))
daily_withdrawn=float(input("Enter the Daily Withdrawn: "))
atm_cash_available = float(input("Enter the  Atm Cash Available: "))

daily_limit=1000.0
if(entered_pin!=actual_pin):
    print("Pin not matched")
    print("Please try again!!")
elif(requested_amount<account_balance):
        print("Insufficient Balance")
elif(daily_withdrawn + requested_amount):
        print("Daily limit Exceeded!")
elif(requested_amount >= atm_cash_available):
        print("Atm Machine Out of Cash")
    