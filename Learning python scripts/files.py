#We can use, interact and open file using python. using the syntax: with open("file") as new_name:
#                                                                     variable_name = new_name.read()

#Note:this wont work here as we do not have a file called welcome.tx, thisis only for example purposes
#with open("welcome.txt") as text_file:
  #text_data = text_file.read()
  #print(text_data)




#we can store each line of a file in a variable by using the .readlines() function:
#with open("how_many_lines.txt") as lines_doc:
  #for line in lines_doc.readlines():  goes through each line using a loop and .readlines()
    #print(line)

                               #readlines() reads the whole file, readline() reads one line of a file


#  .readline() reads the first line in a txt file and in this case it is being saved to first_line
#with open("just_the_first.txt") as first_line_doc:
  #first_line = first_line_doc.readline()
  #second_line = first_line_doc.readline()   #when we use .readline() again, it saves the second line of the txt file to the variable we assigned to it
  #print(first_line, second_line)




#we can use python to write in a file.
#with open("bad_bands.txt", "w") as bad_bands_doc:      #if we the letter "w" as a second argument after the file name, is lets us modifi the file
  #bad_bands = bad_bands_doc.write("All of the bands")    #using .write(), we can write inside the parameters as to what we want. this then changes the file in our directory after we run the script

# "w" is for "write", to write in a file
# "r" is for "read", to read a file
# "a" is for "append", to append a file and new lines in it, rather than overriding it with "w".


#this adds another line to the txt file we specified
#with open("cool_dogs.txt", "a") as cool_dogs_file:
  #cool_dogs_file.write("Air Buddy\n")   #everytime we run the scriptit will add the line again



#we have been using the "with" block to open, append and write with files. the reason is that when we leave the indent of the with block, it closes the file automatically
#old syntax is different, we would have to use the .close() function to close if we do not have a with bloc and indent.
#fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
#fun_cities_file.write("Montréal")

# But we need to remember to close the file
#fun_cities_file.close()



#CSV FILES: we can also interact with csv files.    csv files are just plain text separated by commas.  CSV = Comma Separated Files
#with open("logger.csv") as log_csv_file:
  #print(log_csv_file.read())          #same, syntax, it opens and reads all of the csv file



#we can convert csv files into dictionary, or read them as dictionaries to be able to extract data: 
#import csv      #we will have to import the csv module for this

#birth_date_list = []
#with open("customer_data.csv", newline = "") as customer_data_csv:        #newline = "" simply is used to prevent any problems regarding whitespace in a csv file
    #customers_data = csv.DictReader(customer_data_csv)             #.DictReader reads the csv file as a dictionary
    #for data_row in customers_data:
        #birth_date_list.append(data_row["Birth Dates"])         #this appends the list with the values in the dictionary associated with the given key, in this case "birth dates"




#import csv

#with open("cool_csv.csv") as cool_csv_file:
  #cool_csv_dict = csv.DictReader(cool_csv_file)

  #for row in cool_csv_dict:
    #print(row["Cool Fact"])
    





#IF THE CSV FILE IS NOT SEPARATED BY COMMAS, WE CAN USE THE FOLLOWING:
#import csv


#with open("books.csv") as books_csv:
  #books_reader = csv.DictReader(books_csv, delimiter = "@")      #at the DictReader() function, we added a second argument, which says delimiter = "@", as the data is separated by the delimiter "@"
  #isbn_list = []
  #for row in books_reader:
    #isbn_list.append(row["ISBN"])  #will output the value from the: key = "ISBN"








#WE CAN WRITE CSV FILES ASWELL:

#access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
#fields = ['time', 'address', 'limit']

#import csv

#with open("logger.csv", "w") as logger_csv:             #use the "w" argument to write a csv
  #log_writer = csv.DictWriter(logger_csv, fieldnames = fields)  #insted of DictReader(), we are using DictWriter() to write, with the first argument being the new csv file we want to create, and fieldnames = fields which is our header list above

  #log_writer.writeheader()      #use .writeheader() to create the headers we established for the fieldnames argument
  #for item in access_log:
    #log_writer.writerow(item)   #for every item, we use .writerow() to write the whole of the list of dictionaries, access_log into our new csv file





#json FILES: READING json

#import json                   #we import the json module

#with open("message.json") as message_json:
  #message = json.load(message_json)     #we use the .load() function to unload the json file so python can read it

  #print(message["text"])    #we print a certain object with the key = "text"




#WRITING A json FILE

#data_payload = [     #here we have the dictionary we want to put in a json file
  #{'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   #'follow up': 'But enough talk!'}
#]


#import json

#with open("data.json", "w") as data_json:    #using the "w" argument
  #json.dump(data_payload, data_json)     #we use the json.dump() function with the first argument being the dictionary name and the second argument being the variable name for the json file









#REVIEW


#import csv

#compromised_users = []
#with open("passwords.csv") as password_file:
  #password_csv = csv.DictReader(password_file)
  #for row in password_csv:
    #password_row = row
    #compromised_users.append(password_row["Username"])

#with open("compromised_users.txt", "w") as compromised_user_file:
  #for user in compromised_users:
    #compromised_user_file.write(f"{user}\n")

#import json

#with open("boss_message.json", "w") as boss_message:
  #boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  #json.dump(boss_message_dict, boss_message)

#with open("new_passwords.csv", "w") as new_passwords_obj:
  #slash_null_sig = """
#   _  _     ___   __  ____             
#/ )( \   / __) /  \(_  _)            
#) \/ (  ( (_ \(  O ) )(              
#\____/   \___/ \__/ (__)             
# _  _   __    ___  __ _  ____  ____  
#/ )( \ / _\  / __)(  / )(  __)(    \ 
#) __ (/    \( (__  )  (  ) _)  ) D ( 
#\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
#        ____  __     __   ____  _  _ 
# ___   / ___)(  )   / _\ / ___)/ )( \
#(___)  \___ \/ (_/\/    \\___ \) __ (
#       (____/\____/\_/\_/(____/\_)(_/
# __ _  _  _  __    __                
#(  ( \/ )( \(  )  (  )               
#/    /) \/ (/ (_/\/ (_/\             
#\_)__)\____/\____/\____/
#"""
#  json.dump(slash_null_sig, new_passwords_obj)


