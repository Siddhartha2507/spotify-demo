#project

questions = [
    {
        "question1" : "Who is the director of the movie, Bahubali?",
        "options" : ["A. Rajamouli","B. Koratala Siva ", "C. Sandeep reddy vanga", "D.Maruthi"],
        "answer" : "A"
    }
]

score = 0

# def ask_question(question_bundle):
#     print(question_bundle["question"])
#     for option in question_bundle["questions"]:
#         print(options)

for i, question in enumerate(questions):
    print(f"Question {i+1}: {question["question1"]}")
    for option in question["options"]:
        print(option)
    choice = input("enter your answer:")
    if choice == question["answer"]:
        score += 1

print(f"Your score: {score}")
