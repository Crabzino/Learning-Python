first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]

new_account = print(account_generator(first_name, last_name))




#backwards slash, \, can be used to be able to get python to output quotation marks
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation)



password = "theycallme\"crazy\"91"       #first \ before the quotation mark and the second \ before the second quotation mark you want outputted
print(password)


#WITHOUT USING LEN(), WE MANAGED TO OUTPUT LENGTH OF A WORD
def get_length(word):
  counter = 0
  for letter in word:
    counter += 1
  return counter

print(get_length("test"))




#THIS CHECKS IF A LETTER IS IN A WORD
def letter_check(word, letter):
  for i in word:
    if i == letter:
      return True
  return False

print(letter_check("strawberry", "a"))




#returns common letters
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):  #this means that if a letter in string 1 and letter in string 2 are the same, add it in common if it hasnt been already
      common.append(letter)
  return common




#username generator
def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

#this uses the username to generate a password. it shifts the username index and outputs a password
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(password_generator(username_generator("Elizabeth", "Snowden")))





#DOUBLE COLONS (::)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
new_list = list[::1]     #USING DOUBLE COLONS, IT MEANS THAT IT WILL GO THROUGH THE LIST IN 1 STEP AND PRINT IT OUT
print(new_list)     #output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
new_list2 = list2[::2]     #USING DOUBLE COLONS, IT MEANS THAT IT WILL GO THROUGH THE LIST IN 2 STEPS AND PRINT IT OUT
print(new_list2)   #output [1, 3, 5, 7, 9, 11, 13, 15]


#can do this too
list3 = new_list2[::-1]  #print from reverse



lst = [1, 2, 3, 4, 5]

lst[1:4:2]  # → [2, 4]  start at index 1, stop before index 4, step by 2
lst[4:1:-1] # → [5, 4, 3]  go backwards from index 4 down to (but not including) index 1


#THIS MANUALLY CHECKS IF LIST 1 IS THE SAME AS THE REVERSE OF LIST 2
def reversed_list(lst1, lst2):
    if lst1[::-1] == lst2:
        return True
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


#ANOTHER WAY TO DO IT
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True



#this is a quick and powerful way to check if a string is in another string. using 'in
string = "str"
string2 = "strawberry"
print(string in string2)   #this will output true





#STRING FORMATTING.  
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()     #.title() is to make the first letter capital
poem_author_fixed = poem_author.upper()   #.upper() is to make the whole string capital
                                          #.lower() is to make all of the string lower case

print(poem_title)
print(poem_title_fixed)

print(poem_author)
print(poem_author_fixed)



#.split() splits the words in a string and makes a list
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)        #output ['The', 'sky', 'has', 'given', 'over']



#USING THE SPLIT FUNCTION WITH A ARGUMENT (dilameter, in this case)
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)   #this splits the author lists at the comma making white space in between the commas

#here we want only the lst names in a new list
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])    #this adds only the last names in a list by doing .split() without an argument so it splits at whitespace then it adds the last name only by using index as we know
print("\n") 
print(author_last_names)




#this splits the text into lines and makes a list with each element a different line
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print(spring_storm_lines)



#(\t) is used to make tabs/space in a string
text = "Alice\t25\tParis"

parts = text.split("\t")  #when there are tabs, split can create a list with each element being a new one after the \t
print(parts)




#.join() is the opposite of .split(). it joins elements from a list together. syntax is  (dilameter).join(argument), with argument being the list and the dilameter being the way you want the elemnts joined
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)    #outputs: Black reapers with the sound of steel on stones

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(''.join(my_munequita))  #outputs: MySpanishHarlemMonaLisa





winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)                      
#output All the complicated details
#of the attiring and
#the disattiring are completed!
#A liquid moon
#moves gently among
#the long branches.
#Thus having prepared their buds
#against a sure winter
#the wise trees
#stand sleeping in the cold.

winter_trees_full2 = ",".join(winter_trees_lines)  #can join with comma and space aswell or no commas at all.
print(winter_trees_full2)  #outputs as a csv file
#outputs:  All the complicated details,of the attiring and,the disattiring are completed!,A liquid moon,moves gently among,the long branches.,Thus having prepared their buds,against a sure winter,the wise trees,stand sleeping in the cold.




#THIS CLEANS THE WHITE SPACE USING .strip() FUNCTION
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())  #THIS IS HOW TO USE .strip() WITH A LIST

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)   #THEN USE .join() TO JOIN THEM AND MAKE A FULL STRING





#.replace() CAN BE USED TO REPLACE ANYTHING FROM A STRING TO SOMETHING ELSE.
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")  #replaced tomer with toomer
print(toomer_bio_fixed)

toomer_bio_underscore = toomer_bio.replace(" ", "_")  #replaced the whitespace with an underscore
print(toomer_bio_underscore)





#.find() CAN BE USED TO FIND THE INDEX OF A CERTAIN PART OF A STRING YOU ARE LOOKING FOR. USE A FOR LOOP TO FIND INDEX IN ELEMENT OF A LIST
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")  #output 20. the first index number of the argument we are finding
print(disown_placement)





def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}".format(title, poet)

poem_title_card("I Hear America Singing", "Walt Whitman")
print(poem_title_card)



#.format() IS USED TO ADD VARIABLES TO STRINGS
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)   #we use {} to show where we want the variables to be inputed then use /format() at the end with the function arguments

print(poem_title_card("I Hear America Singing", "Walt Whitman"))  #output: The poem "I Hear America Singing" is written by Walt Whitman.




#.format() ARGUMENTS DO NOT HAVE TO BE IN ORDER. YOU CAN USE KEYWORDS LIKE def function() TO MAKE IT MORE READABLE AND EASIER TO USE
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc                                                                                                                  #keywords in format()

my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")
print(my_beard_description)                      #keywords here






#REVIEW
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
print("\n")
print(highlighted_poems_list)  #makes a element for a list at each comma

highlighted_poems_stripped = []
for poem_info in highlighted_poems_list:
  highlighted_poems_stripped.append(poem_info.strip())
print("\n")
print(highlighted_poems_stripped)    #strips all the whitespace for each element

highlighted_poems_details = []
for info in highlighted_poems_stripped:
  highlighted_poems_details.append(info.split(":"))
print("\n")
print(highlighted_poems_details)  #splits at colon making them separate elements

titles = []
poets = []
dates = []
for item, item1, item2 in highlighted_poems_details:
  titles.append(item)
  poets.append(item1)
  dates.append(item2)
print("\n")
print(titles)
print("\n")                   #makes separate lists for each type of info as seen here
print(poets)
print("\n")
print(dates)
print("\n")      

for poem, poet, date in highlighted_poems_details:
  print("The poem {} was published by {} in {}.".format(poem, poet, date))   #this prints a string for every 1 poem, title and poet there is 