logged_in=True
quiz=True
premium_sub=False
free_trial=True
study_material= premium_sub or free_trial

quiz_access= premium_sub and free_trial 

print(f"Quiz Access Check: {quiz_access}")
print(f"Study Material Access Check: {study_material}")

print("-------------------------------------------------------------------")

if(premium_sub and free_trial):
    print("Quiz Access: Allowed ")
else:
    print("Quiz Access: Denied ")

if(study_material):
    print("Study Material Access: Allowed ")
