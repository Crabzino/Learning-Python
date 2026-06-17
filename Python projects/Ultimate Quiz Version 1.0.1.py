welcome_message = """
==================================================
Welcome to the first version of the ultimate quiz!
==================================================
"""
print(welcome_message)


questions_for_quiz = [
    ["What is the capital of America?", "washington dc"],
    ["What is the capital of England?", "london"],
    ["What is the ugliest, dumbest, most devilish, heinous country in the world?", "israel"],
    ["What is the religion of peace?", "islam"],
    ["What is the biggest car brand in the world?", "toyota"],
    ["Who was the last prophet?", "muhammad peace and blessings be upon him"],
]

#Score Tracking, Wrong Answer Tracking
score = 0
wrong_question = []

for question, answer in questions_for_quiz:                                                 #1.0.1 update, we use a cleaner loop, allowing for better readability and user efficiency
    user_answer = input(f"\n{question}: ").lower().strip()

    if user_answer == answer:                       
        print("Correct!")
        score += 1
    else:
        print(f"Wrong, the correct answer is {answer}")
        wrong_question.append(question)


print("\n====================================")
print("That is now the end of Ultimate Quiz")
print("====================================\n")


#statement and score
if score == len(questions_for_quiz):
    print(f"Congratulations! you got {score}/{len(questions_for_quiz)}\n")
elif score > 3:
    print(f"Nearly there, you got {score}/{len(questions_for_quiz)}\n")
elif score > 0:
    print(f"Mate you are so bad, go back to nursery. You got {score}/{len(questions_for_quiz)}\n")
elif score == 0:
    print(f"Honestly, if I can output a laughing emoji, I would. Get out of my face. You got {score}/{len(questions_for_quiz)}\n")

#show wrong answered questions
if score < len(questions_for_quiz):
 print("Questions you got wrong:")
 for q in wrong_question:
     print(f"  {q}")
else:
    print("Congrats, no questions wrong.")