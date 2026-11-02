prices = [140, 270, 100, 470, 320]

lists = []
for price in prices:
    if price > 300:
        lists.append("Expensive")
    else:
        lists.append("Affordable")

prices_above_200 = []
for price in prices:
    if price > 200:
        prices_above_200.append(price)

print(lists)
print(prices_above_200)