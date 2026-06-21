#Strings Review:

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index > -1 and end_index > -1:
    return word[start_index + 1 : end_index]
  else:
    return word
  
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"





def x_length_words(sentence, x):
  sentence_array = sentence.split(" ")
  for word in sentence_array:
    if len(word) < x:
      return False
    else:
      return True



# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True







def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False

#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False


#Or can be done like this
#def check_for_name(sentence, name):
  #return name.lower() in sentence.lower()





def every_other_letter(word):
  resulting_string = ""
  for letter in word[::2]:
    resulting_string += letter
  return resulting_string



# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 


#or like this
#def every_other_letter(word):
  #every_other = ""
  #for i in range(0, len(word), 2):
    #every_other += word[i]
  #return every_other








def reverse_string(word):
  reversed_word = ""
  for letter in word[::-1]:
    reversed_word += letter
  return reversed_word
  
# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print








def make_spoonerism(word1, word2):
  word1_first = word1[0]
  word2_first = word2[0]
  word1_rest = word1[1::1]
  word2_rest = word2[1::1]
  return f"{word2_first}{word1_rest} {word1_first}{word2_rest}"


#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a


#or like this
#def make_spoonerism(word1, word2):
  #return f"{word2[0]}{word1[1::1]} {word1[0]}{word2[1::1]}"





def add_exclamation(word):
  while len(word) <= 20:
    word += "!"
  return word
 


# Uncomment these function calls to test your function:
#print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
#print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn










#DICTIONARIES REVIEW:

def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():                           #this function returns the key with the largest value
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
#print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"





#makes a dictionary of strings in words list with their length being the value
def word_length_dictionary(words):
  new_dictionary = {}
  for word in words:
    new_dictionary.update({word: len(word)})
  return new_dictionary


# Uncomment these function calls to test your  function:
#print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
#print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}






def frequency_dictionary(words):
  frequent_dictionary = {}
  for word in words:                                          #for every same word in list, the dictionary key will be the word and the value will be the amount of time the key appears in the list
    if not word in frequent_dictionary:
      frequent_dictionary[word] = 0
    frequent_dictionary[word] += 1
  return frequent_dictionary


# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}






def unique_values(my_dictionary):
  unique_item = []
  for item in my_dictionary.values():
    if item not in unique_item:                                       #returns the amount of unique values in a dictionary
      unique_item.append(item)
  return len(unique_item)


# Uncomment these function calls to test your  function:
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1






def count_first_letter(names):
  letters = {}
  for key in names.keys():                               #this function adds to a new dictionary, the first letter of a key in the old dictionary if it isnt their already, and the value will be the amount of people who have the same start letter surname fro the old dictionary
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# Uncomment these function calls to test your  function:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}