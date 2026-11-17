gross_prices = [45.0, 120.0, 85.5, 250.0, 15.0, 199.99]
total_price=[ round(price * 0.85 * 1.08 ,2)if (price >100) else round(price * 0.95 * 1.08,2) for price in gross_prices]
print(total_price)