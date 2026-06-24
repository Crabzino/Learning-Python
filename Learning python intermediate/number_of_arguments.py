#THE * METHOD: If we have multiple arguments for a function, we can you the asterisk ,*, for as much arguments as we want:  (args), short for arguments
#UNPACKING OPERTOR

def food_order(*customer_order):   #takes as much arguments as we want
    print(customer_order)


food_order("Orange Juice", "Apple Juice", "Scrambled Eggs", "Pancakes")    #outputs this whole tuple



def shout_strings(*args):
  for argument in args:      #using a loop to output each element in uppercase
    print(argument.upper())

shout_strings('Working on', 'learning', 'argument unpacking!')






def example_func(length, *sentences):
   for sentence in sentences:
      print(sentence[:length])


example_func(12, "This is a crazy situation", "Our comunication has", "Been cut off for some reason")  #for each *sentences argument, it cuts of the string at the length we provided

#output: This is a cr
#        Our comunica
#        Been cut off








tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False):   #assigns table info
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Write your code below: 
def assign_and_print_order(table_number, *order_items):     #this function uses the unpacking operator to display all the food menu arguments
  tables[table_number]['order'] = order_items       #it assigns it to the table
  for order_item in order_items:  #prints out the order for the kitchen
    print(order_item)

assign_table(2, "Arwa", True)                      
assign_and_print_order(2, "Steak", "Seabass", "Wine Bottle")           

print(tables)



#The ** METHOD (kwargs)   we can use ** to have unlimited arguments and key word arguments:
# ** genereate a standard dictionary

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


def assign_food_items(**order_items):  #use ** here 
  print(order_items)

  food = order_items.get('food')     #we have avariables here
  drinks = order_items.get('drinks')

  print(food)
  print(drinks)
  


assign_food_items(food='Pancakes, Poached Egg', drinks='Water')    #we assign to those variables what we want










tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)


def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks


print('\n --- tables after update --- \n',)
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)