list=["Alice","Bob","Charlie","David","Alice"]

a =list[2]="chris"
b = list.count("Alice")
c = list.pop()
d = list.pop(1)
e = list.remove("Alice")
f= list.clear()
print(f"changed name: {list}")
print(f"Count Alice: {b}")
print(f"Pop: {c}")
print(f"Pop index: {d}")
print(f"Alice remove: {e}")
print(f"List Clear: {f}")
print(list)

