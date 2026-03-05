questions = [
    ("What is 2 + 2?", "4"),
    ("What is capital of India?", "Delhi"),
    ("What is 5 * 6?", "30"),
    ("What is Python?", "Programming"),
    ("What is 10 - 5?", "5")
]

score = 0

for question, answer in questions:
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1

print("\nYour final score is:", score, "/", len(questions))
