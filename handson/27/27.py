store = {"Laptop":8,"mouse":0,"keyboard" : 15,"monitor":5}
avail_prod = [product for product, qty in store.items() if qty > 0]
unique_quan = sorted({qty for qty in store.values()})
inventory_status = {product:"Available" if qty > 0 else "Out of Stock" for product, qty in store.items()}
print("Available Products:", avail_prod)
print("Unique Stock Quantities:", unique_quan)
print("Inventory Status:", inventory_status)

