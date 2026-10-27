list=["Milk","bread","Eggs"]
friend_list=["bread","Biscuits"]


list_append=list.append("Butter")
list_insert=list.insert(1,"Rice")
list_remove=list.remove("bread")
extend_list=list.extend(friend_list)

slicing=list[:4]
sorting=list.sort()
reverse_sorting=list.sort(reverse=True)

print(f"Friend list: {friend_list}")
print(f"slicing: {slicing}")
print(f"Sorting {sorting}")
print(f"Reverse Sorting: {reverse_sorting}")


