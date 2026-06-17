#FIRST ONE: Insert
#we use insert to add an element to a specific area in the list using the index

thelist_1 = [345, 8463, 35, 23, 78564, 1234, 636523]

thelist_1.insert(3, "Goose")  #the format is: listvariable.insert(index, element)
print(thelist_1) #it will appear after the number 35


#SECOND ONE: pop
#we use the pop method to remove any element we want from a list.
thelist_1.pop(1) #this will remove the second one
print(thelist_1)

thelist_1.pop() #if we keep it empty, it will simply remove the last element form a list. assign it to a variable and print it to see what was removed
print(thelist_1)



data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)



#THIRD ONE: range and list functions: can make a range from a 0 to a certain number:
mylist_2 = range(100)
print(mylist_2)

print(list(mylist_2))  #use the list function to actually print out the whole range not just '0, 100'


#SEVENTH ONE: Sorting lists. we can use .sort to print out a list in alphabetical order or small to large number order.
numb_list_ultra = ["Mike", "China", "John", "Fort", "America"]
numb_list_ultra_order = numb_list_ultra.sort()
print(numb_list_ultra_order)

