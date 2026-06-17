last_semester_gradebook = []

num_subjects = int(input("How many subjects did you take last semester? "))

for i in range(num_subjects):
    subject = input(f"What was subject {i + 1}? ")
    grade = input(f"What grade did you get in {subject}? ")

    # Convert to number if possible
    try:
        grade = int(grade)
    except ValueError:
        pass

    last_semester_gradebook.append([subject, grade])

print("\nYour gradebook:")
print(last_semester_gradebook)