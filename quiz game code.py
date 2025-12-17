questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["Python", "HTML", "CSS", "C"],
        "answer": "Python"
    },
    {
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "Automatic Internet", "Advanced Input", "None"],
        "answer": "Artificial Intelligence"
    },
    { 
        "question": "Who is known as the father of AI?",
        "options": ["Alan Turing", "John McCarthy", "Geoffrey Hinton", "Andrew Ng"],
        "answer": "John McCarthy"
    },
    {
        "question": "Which of the following is a popular AI framework?",
        "options": ["TensorFlow", "Django", "React", "Laravel"],
        "answer": "TensorFlow"
    },
    { 
        "question": "What is machine learning?",
        "options": ["A subset of AI", "A programming language", "A type of database", "A web framework"],
        "answer": "A subset of AI"
    },
]      

score = 0

for q in questions:
    print("\n" + q["question"])
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")

    choice = int(input("Enter option number: "))
    user_answer = q["options"][choice - 1]

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong")

print("\nQuiz Finished!")
print(f"Your score: {score}/{len(questions)}")  
