#DICTIONARIES ARE a way to map data together: syntax is {key: Value}. Notice that we use curly braces to store them

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}   #living room is the key, and 21 is the value assigned to it
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

#print(sensors) #outputs the dictionary



#dictionaries keys can be numbers aswell:   KEYS CAN NOT BE LISTS BECAUSE LISTS CAN CHANGE SO ITS NOT A RELIABLE KEY. LISTS ARE UNHASHABLE
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}


#values can be any type. it can be a list, a number or string:
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
#in this case, the list is the value, representing the students in different classes



#we can also mix and match key and value types:
person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]} #we have 3 different keys here and 3 different values, 1 integer, 1 string and 1 list



translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"} #this maps the english key word to a different language 



#dictionaries can be empty for when we want to add keys and values to it later on
my_empty_dictionary = {}


#you can add noew kays and values to an empty dictionary or you can add to an existing one. Syntax: dictionary[key] = value

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8  #zebra being the key in square brackets and 8 is the value after the equal sign
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
#print(animals_in_zoo)    #outputs the dictionary



#to add multiple keys and values to a dictionary, we use the .update() method  syntax: dictionary.update({key: value, key: value, key: value})
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 24, "attic": 28, "basement": 19})
#print(sensors)


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})



#the syntax: dictionary[key] = value adds a key with assigned value to an existing dictionary. but if the key already exists, it override the current value with the new one.
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
#print(menu)    #this overrides the 3 to a 5 for oatmeal



oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"  #this adds a new key and value
oscar_winners["Best Picture"] = "Moonlight"    #this overrides the current value associated with best picture to the new one




#if we have two lists and we want to combine them together in a dictionary, we can do it like this
students = ["John", "Lola", "James", "jack", "Ali", "Rhys", "Lily"]
ages = [15, 45, 23, 12, 56, 34, 59]
student_data = {}

for student, age in zip(students, ages):  #zip function to combine two lists together
    student_data.update({student: age})
#print(student_data)   #outputs the new list


#dictionary comprehension
students_comp = ["John", "Lola", "James", "jack", "Ali", "Rhys", "Lily"]
ages_comp = [15, 45, 23, 12, 56, 34, 59]
student_data_comp = {student: age for student, age in zip(students_comp, ages_comp)} #dictionary comprehension
#print(student_data_comp)


drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drink: caffe for drink, caffe in zipped_drinks}




#REVIEW
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: playcount for song, playcount in zip(songs, playcounts)}
#print(plays)
#print("\n")

plays["Purple Haze"] = 1
plays["Respect"] += 5  #this adds an additional 5 plays to the key
#print(plays)
#print("\n")

library = {"The Best Songs": plays, "Sunday Feelings": {}}  #this outputs the value of the best songs to be the dictionary called plays. sunday feelings has an empty value
#print(library)
