#def createStudent(name, age, grades=[]):
#    return {
#        'name': name,
#        'age': age,
#        'grades': grades
#    }


#chrisley = createStudent('Chrisley', 15)
#dallas = createStudent('Dallas', 16)


def addGrade(student, grade):
    student["grades"].append(grade)
    # To help visualize the grades we have added a print statement
    print(student["grades"])


#addGrade(chrisley, 90)      #this is a gotcha, where both of there grades are added in on list.
#addGrade(dallas, 100)






def createStudent(name, age, grades=None):
  if grades is None:      #using the non method, this sorts it out
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }



chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)