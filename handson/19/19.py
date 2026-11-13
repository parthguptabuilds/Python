def show_appointment_status(appointment_id, status="confirmed"):
    print("Patient",appointment_id,":",status)

show_appointment_status(int(input("Enter Your Id: ")))
show_appointment_status(int(input("Enter Your Id: ")),"Completed")