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



#we can obtain a value from dictionary by printing the key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

#print(zodiac_elements["earth"])
#print(zodiac_elements["fire"])




#invalid keys:  IF WE TRIED TO PRINT A VALUE BY USING A KEY THAT DOES NOT EXIST, IT WILL OUTPUT AN ERROR. TO AVOID THAT USE AN IF STATEMENT
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"   #it will work now because we added the key

#if "energy" in zodiac_elements:      #it will only output the print statement if the key exists
  #print(zodiac_elements["energy"])





#WE CAN USE THE .get() METHOD TO GET A KEY'S VALUE. IF THE KEY DOES NOT EXIST IT WILL OUTPUT none. OR YOU CAN ASSIGN WHAT IT SHOULD OUTPUT IF IT DOES NOT EXIST
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}


tc_id = user_ids.get("teraCoder", 100000) #this will output the value of the key as the key exists. the 100000 that is after the key is what would be outputed if the key does not exists
#print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)  #the output will be 100000 as the key does not exist
#print(stack_id)






building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")



#print(building_heights.get('Shanghai Tower', 0)) # Prints 632
#print(building_heights.get('Mt Olympus', 0)) # Prints 0
#print(building_heights.get('Kilimanjaro', 'No Value')) # Prints 'No Value'




#WE CAN USE THE .pop() METHOD TO REMOVE KEYS FROM THE DICTIONARIES
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)  #if the key exists, it adds the value of the key to the health_points number and then removes. if it does not exist it adds 0 which is the number after the key in .pop()
#print(health_points)
#print(available_items)

health_points += available_items.pop("power stew", 0)  #same here
health_points += available_items.pop("mystic bread", 0)   #mystic bread does not exist, so it added 0 to health_points

#print(available_items, health_points)




#HOW TO GET ALL KEYS WITHOUT VALUES   .keys()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#print(list(user_ids))   #using list, this will generate a list of the keys without the values

#for user in user_ids.keys():    #this will generate a dict_keys view of the keys in the dictionary
    #print(user)



#test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#for student in test_scores.keys():
 #print(student)





user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}


users = user_ids.keys()      #prints all keys
lessons = num_exercises.keys()  

#print(users)
#print(lessons)





#HOW TO GET ALL VALUES WITHOUT KEYS       .values()
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

#for score_list in test_scores.values():
 #print(score_list)   #outputs all values

print(list(test_scores.values()))  #outputs all values as a list



#this adds all values of each key to the total_exercises number 
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for num in num_exercises.values():
  total_exercises += num

#print(total_exercises)





#HOW TO GET BOTH KEYS AND VALUES     .items()
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

#for company, value in biggest_brands.items():   #using the .item(), it is iterating through each key and value
   #print(f"{company} has a whopping value of {value} billion dollars")   #this will output a strings and for each, it contains company and value assigned to each



#another example
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}


#for occupation, percent in pct_women_in_occupation.items():
  #print(f"Women make up {percent} percent of {occupation}s.")






#REVIEW
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)   #this removes the key and its value from the above list and adds the value here to the new assigned key
spread["present"] = tarot.pop(22)   #output: {"present": "The Fool"}
spread["future"] = tarot.pop(10)

#for key, value in spread.items():
  #print(f"Your {key} is the {value} card.")       # Your present is the The Fool card.