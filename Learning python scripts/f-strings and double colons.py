name = "John"
age = 28

full_statement = f"Hi, my name is {name} and I am {age} years old."
print(full_statement)



x = 17
print(f"what is x multiplied by x?: {x ** 2}")
      



price = 3.14159
print(f"Price: {price:.2f}")   # Price: 3.14   (2 decimal places)

n = 1000000
print(f"Big number: {n:,}")   #outputs 1,000,000 with comma separators



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