#Learning Classes

#Classes are a template for data types. it tells us the kind of information that they will hold and how programmers interact with them:
class Facade:
  pass       #we used pass here so the terminal does not cause an indent error



#we got to create an instance of the class, similar to calling a function
class Facade: 
  pass

facade_1 = Facade()   #we assign the class with brackets to a variable



#A class instance is also called an object. The pattern of defining classes and creating objects is called OOP: Object Oriented Programming. Instantiation takes a class and turns it into an object.
#type() function does the opposite of that. When called with an object, it returns the class associated with it

class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)
print(facade_1_type)





#For the data to be available for every instance of a class, we can use class variables like below:
class Fighters:
  title = "Captain"     #Captain is associated with the variable title      #can be integers aswell

luffy = Fighters()   #we instantiate the variable luffy with the fighters()
print(luffy.title)    #output: Captain





#methods are functions defined in classes. first argument should always be 'self'.  the functions are indented to be under classes
class Food:
  highest_food_rating = 10

  def indian_food(self):
    print("This Curry has by far the highest rating, A whopping {} out of 10.".format(self.highest_food_rating))   #the argument self is followed by the class variable we assigned above


lamb_curry = Food()     #we instantiate our variable here with the class
lamb_curry.indian_food()   #this will output the string associated in the indian_food() function




#or we can just have a method function
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
  




#this one has more than one argument
class Weight:
  lb_in_kg = 2.205
  def converter(self, lbs):
    return lbs * self.lb_in_kg
  
my_lb = Weight()
my_lb_5 = my_lb.converter(5)  #we do not need to provide more than one argument as self is implicitly passed
print(my_lb_5)






#Another example
class Circle:
  pi = 3.14

  def area(self, radius):
    return self.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(f"The areas of the pizza, teaching table and round room building is as follows: {pizza_area}, {teaching_table_area} and {round_room_area}.")







#Using the '__init__' method to instantiate a class object, so would not have to call the function itself within the class
class Menu:
  def __init__(self, num_of_people):          #use '__init__' after def and before the parameters
    food_menu = "Here is the menu: Lamb, Beef, Chicken."
    for num in range(num_of_people):
      print(food_menu)

booking1 = Menu(4)     #variable to instantiate the class and add the argument  for num_of_people parameter



#Another example
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle(36)






#Instance Variables:  each instance of a class can hold different kinds of data
class Store:
  pass   #we use pass to not cause an indentation error

alternative_rocks = Store()   #use the Store class to instantiate the object
isabelles_ices = Store()      #sane here

alternative_rocks.store_name = "Alternative Rocks"     #we created a .store_name method to holde to types of data
isabelles_ices.store_name = "Isabelle's Ices"          #same here







#attribute functions
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")


#we can use hasattr() to see if an object has an attribute. syntax: hasattr(object, “attribute”)
hasattr(attributeless, "fake_attribute")
# returns False



#getattr() would return the value of given object and attribute
getattr(attributeless, "other_fake_attribute", 800)   #we use the defualt parameter at the end if the object has no attribute, it would return the 800
# returns 800, the default value





#using the hasattr() to see if an element in a list has the count attribute
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

#output
#<class 'dict'> does not have the count attribute :(
#<class 'str'> has the count attribute!
#<class 'int'> does not have the count attribute :(
#<class 'list'> has the count attribute!






class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"










#using self properly. it is a very powerful tool
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())






#Using dir() to find all the attributes associated with an object:
print(dir(5))



def this_function_is_an_object(v1, v2):
  return v1 + v2

print(dir(this_function_is_an_object))







#here we added the repr() function which allows to output the representation of an object
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
   return f"Circle with radius {self.radius}."
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
 
                                                   #from this:  "<__main__.Employee object at 0x104e88390>" to this:  Circle with radius 6.0.   Circle with radius 18.0.  Circle with radius 5730.0.
print(medium_pizza)
print(teaching_table)
print(round_room)





#REVIEW
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
      if type(grade) is Grade:
        self.grades.append(grade)
  
class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score
 

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
