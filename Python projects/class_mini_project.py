class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items  #a list
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return f"{self.name} menu is available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in self.items.keys():
        if item in purchased_items:
            total_price += self.items[item]
    return f"The total price is ${total_price}."
    

brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch_menu = Menu("brunch", brunch_items, 1100, 1600)



early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird_menu = Menu("earley bird", early_bird_items, 1500, 1800)



dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

dinner_menu = Menu("dinner", dinner_items, 1700, 2300)



kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids_menu = Menu("kids", kids_items, 1100, 2100)


print(brunch_menu)
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))



class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus  # list

  def __repr__(self):
    return f"The address of the restaurant is {self.address}."

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu




flagship_store_address = "1232 West End Road"
new_installment_address = "12 East Mulberry Street"
franchise_menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise(flagship_store_address, franchise_menus)
new_installment = Franchise(new_installment_address, franchise_menus)

#print(new_installment)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(2100))




class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises  #a list
    

business1_name = "Basta Fazoolin' with my Heart"
business1_franchises = [flagship_store, new_installment] 
business1 = Business(business1_name, business1_franchises)


take_a_arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a' Arepa", take_a_arepa_items, 1000, 2000)


arepas_place_location = "189 Fitzgerald Avenue"
arepas_place_menus = [arepas_menu]
arepas_place = Franchise(arepas_place_location, arepas_menu)


business2_name = "Take a' Arepa"
business2_franchises = [arepas_place]
business2 = Business(business2_name, business2_franchises)