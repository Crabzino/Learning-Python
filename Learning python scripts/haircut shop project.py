hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price

average_price = total_price / len(prices)
print(f"Average haircut price: {average_price}")

new_prices = [num - 5 for num in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: ${total_revenue}")

average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: ${average_daily_revenue}")

#hairstyle_and_price = zip(hairstyles, prices)
#listed_hair_style_and_price = list(hairstyle_and_price)

cuts_under_30 = []
for i in range(len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append([hairstyles[i], new_prices[i]])
print(cuts_under_30)

#cuts_under_30 = [[hairstyles[i], new_prices[i]] for i in range(len(new_prices)) if new_prices[i] < 30]
#print(cuts_under_30)