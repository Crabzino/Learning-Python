#Functions help when you need to repeat code al the time so we 'define' it then 'call' it when we need the code

food_menu_list = ["beef", "lamb", "chicken", "duck", "goose", "turskey", "salmon"]
def food_menu():            #we started with 'def' to define and the variable 'food_menu' is the call name
  print("       Here is our menu:")
  print(f"      {food_menu_list}")
  
  
food_menu()  #when we need those lines of code and that function, all we need to do is type the call name with brackets



def destination(chosen):    #the variable in the brackets is the parameter. 
  print("Welcome")
  print(f"I see you would like to go to {chosen}.") #whatever the input is, it will occur

destination("africa")








def choose_food(foodchoice1, foodchoice2):     #you can add more than one parameter. as much as you like. here there is two. it is important that the parameters are in order of excucution
  print(f"No worries, I will prepare the {foodchoice1} and {foodchoice2} for you.")


foodchoice1 = input("What would you like for your first meal?")
foodchoice2 = input("What would you like for your second meal?")

choose_food(foodchoice1, foodchoice2)




def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  
  
  return trip_total  #return will mean that when we call the function with the parameters answered, it will return and output the trip total

# Step 5: call your function
print(calculate_expenses(200, 100, 100, 5))




def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"): #we can set the default variable for final destination if it wont change by
  print("Here is what your trip will look like!")                                           #  writing it with keyword = input
  print(f"First, we will stop in {first_destination}, then {second_destination} and lastly {final_destination}")


trip_planner("France", "Germany", "Denmark")   #looking at the positional argument it will output dependent on the order of parameters
trip_planner("Denmark", "France", "Germany")   #also notice how putting a new parameter for the final destination overrides the original one

trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")  #using keywords means we do not have to place the parameters in order

trip_planner("Brooklyn", "Queens") #not placing a 3rd parameter means the function will use the one already defaulted



#functions are also built in to python like:
# str, len, max(), min(), sorted etc. these are functions and we have been using some of them

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)    #max price printed

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)    #minimum price printed

rounded_price = round(tshirt_price, 1)   #using round, you can round a number to any amount of decimal places by writing round(variable, digit).  (digit) being the number of decimal places
print(rounded_price)



def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate             #this is a returned function value. it allows us to put the return function in a form of a variable

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print(f"100 dollars in US currency would give you {new_zealand_exchange} New Zealand dollars")



current_budget = 3500.75
shirt_expense = 9

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))  #will output statment with budget

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense     #this function calculates budget after expense deducted

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)  #we then simply assigned it to a new variable, so this variable is the new budget after expense

print_remaining_budget(new_budget_after_shirt)  #we then added that back to the first function so it will print it with the message




food_for_days = [["Monday", "Lamb"], ["Tuesday", "Chicken"], ["Wednesday", "Beef"], ["Thursday", "Duck"], ["Friday", "Squid"]]

def food_for_each_day(food):
  for i in range(5):
    foodvariable = print(f"{food[i][0]}, we will eat {food[i][1]}")
  return foodvariable                                                     #MAY SEEM MESSY BUT I AM JUST PRACTICING VARIABLES IN FUNCTIONS

final_food_variable = food_for_each_day(food_for_days)



food_for_days = [
    ["Monday", "Lamb"],
    ["Tuesday", "Chicken"],
    ["Wednesday", "Beef"],
    ["Thursday", "Duck"],                                #THIS ONE HERE IS THE CLEANER VERSION OF THE CODE ABOVE
    ["Friday", "Squid"]
]

def food_for_each_day(food):
    for day, meal in food:
        print(f"{day}, we will eat {meal}")

food_for_each_day(food_for_days)




#THIS IS TO SHOW HOW YOU DO MULTI RETURNS
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third  #list the multiple ones you want to return

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()  #make new variables and make it equal to the function
                                                                     #the reason is that we can use each string separately rather than printing them all together
print(most_popular1)
print(most_popular2)
print(most_popular3)





def trip_planner_welcome(name):
  print(f"Welcome to tripplanner v1.0 {name}")
trip_planner_welcome("Adam")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)                                                               #THIS IS A BASIC FUNCTION AND CALL SETUP
  return rounded_time
estimate = estimated_time_rounded(10.6)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {estimated_time} hours")
destination_setup("London", "New York", estimate, mode_of_transport = "Private Jet")




#Lambda functiions: lambda functions are used for small functions that only output one expression.  lambda [argument]: [expression]
solved = lambda x, b: x * 2 - b

solved_equation = solved(7, 2)
print(solved_equation)  #this will output 12


answered_statement = lambda name: f"Hello {name}."
print(answered_statement("John"))  #this will output hello john


#MAP FUNCTION WITH LAMBDA
menu_price = [2, 3, 5, 10, 6, 7]
menu_price_inflated = list(map(lambda x: x * 2 + 3, menu_price))
print(menu_price_inflated)   #this outputs the whole menu_price list but with the new calculation of x * 2 + 3


#FILTER FUNCTION WITH LAMBDA
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
odd_numbers = list(filter(lambda x: not x % 2 == 0, numbers))  #this will go through the list and identify all numbers that have a remainder, essentially printing out all odd numbes
print(odd_numbers)    #outputs all odd numbers from the numbers list



#SORTED FUNCTION WITH LAMBDA
city_rank = [["London", "L", 19], ["Texas", "T", 7], ["Beirut", "B", 12]]
city_rank_sorted = sorted(city_rank, key = lambda x: x[2])  #this is sorting the order of the sublists by using the lambda as a key to establish that the third element is the decider from small to big
print(city_rank_sorted)  #this will rearrange the lists  being order of texas, beirut, london



#THE MAP FUNCTION:
def updated_num(x):
  return x ** 2 + 5
  
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
updated_num_list = list(map(updated_num, num_list))   #using our updated_num function, we can make a new variable and map a new list using map[function, list]
print(updated_num_list)



# Converting strings to integers 

str_nums = ['1', '2', '3', '4', '5'] 

int_nums = list(map(int, str_nums))    #converting str to int with map function

print(int_nums)  # Output: [1, 2, 3, 4, 5] 



words = ['apple', 'banana', 'cherry'] 

word_lengths = list(map(len, words))   #map function for converting strigs to the integer of the length of the words

print(word_lengths)  # Output: [5, 6, 6]



list1 = [4, 7, 2, 89, 23, 5, 67]
list2 = [23, 45, 67, 89, 23, 34, 56]

addedlist = list(map(lambda x, y: x + y, list1, list2))  #we can use multipl lists and use lambda with map function to add two lists together as an example
print(addedlist) 



 #REMEMBER WE HAVE THESE AS ALTERNATIVES TO MAP FUNCTION
#List Comprehensions: Often more readable for simple operations.


#doubled = [x * 2 for x in numbers] 


#Generator Expressions: Similar to list comprehensions but return an iterator.

#doubled = (x * 2 for x in numbers) 


# For Loops: More verbose but sometimes clearer for complex operations.

#doubled = [] 

#for x in numbers: 

   #doubled.append(x * 2) 





#MINI FUNCTIONS PROJECT FROM CODECADEMY

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print(f"The GE train supplies {train_force} Newtons of force")

def get_energy(mass, c = 3 * 10 ** 8):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass)
bomb_energy_with_commas = f"{bomb_energy: ,}"

print(f"A 1kg bomb supplies {bomb_energy_with_commas} Joules.")

def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train does {train_work: ,} Joules of work over {train_distance} meters.")


#A FUNCTION WHERE THE COMBINATION OF THE LAST TWO ELEMENTS ARE ADDED TO THE END OF THE LIST THREE TIMES
def append_sum(my_list):
  for i in range(3):
    my_list.append(sum(my_list[-2:]))
  return my_list

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))




def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

    
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))





#SORTING A COMBINED LIST
def combine_sort(my_list1, my_list2):
  new_list = (my_list1 + my_list2)
  new_list.sort()
  return new_list

#OR YOU CAN DO IT THIS WAY
def combine_sort2(my_list1, my_list2):
  return sorted(my_list1 + my_list2)
  

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))