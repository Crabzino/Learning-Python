#USING THE 'zip' FUNCTION TO COMBINE LISTS:
food = ["Lamb", "Beef", "Chicken", "Duck", "Turkey"]
prices = [8, 7, 5, 8, 10]

food_and_prices = zip(food, prices) #this combines the two but stores it in a 'zip object'
print(food_and_prices)

converted_food_and_prices = list(food_and_prices)  #to use it, we convert the zip object by using the 'list' function
print(converted_food_and_prices) #prints out the usable list with list containing sublists of each food and its price
#notice the sublists have been converted to tuples as they are using ()
