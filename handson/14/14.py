import copy

list = [["Laptop", "Monitor"], "Available"]


deep_copy = copy.deepcopy(list)

list[1] = "Assigned"
assigned = list
assigned[0].append("Keyboard")
assigned[1] = "Assigned"

shallow = list.copy()
shallow[0].append("Mouse")
shallow[1] = "Shallow"


deep_copy[0].append("Printer")
deep_copy[1] = "Deep"


print(f"Original: {list}")
print(f"Assigned: {assigned}")
print(f"Shallow:  {shallow}")
print(f"Deep:     {deep_copy}")