shipment_codes = ["A120", "B245", "A198", "C310", "B278"]
unique_zones = sorted({code[0] for code in shipment_codes})
print("Unique Warehouse Zones:", unique_zones)
vehicle_data = {"zone_a": 12, "zone_b": 5, "zone_c": 18, "zone_d": 9}
available_vehicle_zones = {key.upper(): value for key, value in vehicle_data.items() if value >= 10}
print("Available Vehicle Zones:", available_vehicle_zones)