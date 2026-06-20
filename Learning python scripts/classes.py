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