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
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
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