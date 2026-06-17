citylist = ["new york", "glasgow", "belfast", "london", "reading", "manchester", "birmingham"]
for city in citylist:
  print(city)

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1



students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  #students_period_A.append(student)
  print(student)



#THIS CODE KEEPS ON REMOVING THE FIRST NUMBER IN THE LIST UNTIL IT IS ODD
def delete_starting_evens(my_list):
  while len(my_list) > 0 and my_list[0] % 2 == 0:
    my_list = my_list[1:]
  return my_list
 


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))




#THIS CODE ADDS ALL THE NUMBERS WITH ODD INDEX TO A NEW LIST
def odd_indices(my_list):
  odd_index = []
  for i in range(len(my_list)):
    if i % 2 != 0:
      odd_index.append(my_list[i])
  return odd_index


print(odd_indices([4, 3, 7, 10, 11, -2]))


#OR YOU CAN DO IT LIKE THIS
def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list




#THIS RAISES EACH BASE TO EACH POWER
def exponents(bases, powers):
  raised = []
  for base in bases:
    for power in powers:
      raised.append(base ** power)
  return raised

print(exponents([2, 3, 4], [1, 2, 3]))



#RETURNS LIST WITH BIGGER SUM
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))



#EASIER< BETTER AND QUICKER WAY TO WRITE IT
def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))




#THIS KEEPS ADDING ELEMENTS IN LIST UNTIL THE SUM IS GREATER THAN 9000, THEN IT WILL BREAK
def over_nine_thousand(lst):
  sumofnum = 0
  for num in lst:
    sumofnum += num
    if sumofnum > 9000:
      break
  return sumofnum
    

print(over_nine_thousand([8000, 900, 120, 5000]))




#HERE, WE HAVE SET MAXIMUM NUMBER DEFAULT TO FIRST ELEMENT IN LIST. IF THE LOOP FINDS A BIGGER NUMBER, THE NEW MAX WILL BE UPDATED
def max_num(nums):
  maxnum = nums[0]
  for num in nums:
    if num > maxnum:
      maxnum = num
  return maxnum

print(max_num([50, -10, 0, 75, 20]))



#THIS LISTS THE INDICES IN NEW LIST WITH NUMBERS THAT MATCH
def same_values(lst1, lst2):
  matched_indices = []
  for num in range(len(lst1)):
    if lst1[num] == lst2[num]:
      matched_indices.append(num)
  return matched_indices
  
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))