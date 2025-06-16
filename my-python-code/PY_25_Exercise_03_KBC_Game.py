# Simulates a Kaun Banega Crorepati-style quiz game

# List of questions, choices, and correct answers
questions = [
    {
        "question": "What is the full name of South Korea?",
        "choices": ["1: South Korea", "2: Korea", "3: Republic of Korea", "4: People's Republic of Korea"],
        "correct": 3,
        "prize": 1000
    },
    {
        "question": "What is the capital of India?",
        "choices": ["1: Mumbai", "2: Delhi", "3: Kanpur", "4: Chennai"],
        "correct": 2,
        "prize": 2000
    }
]

# Initialize prize money
total_prize = 0

# Welcome message
print("Hello, Sir/Madam! Welcome to Kaun Banega Crorepati!")

# Iterate through questions
for i, q in enumerate(questions, 1):
    print(f"\nQuestion No. {i} for Rs.{q['prize']}")
    print(q["question"])

    for choice in q["choices"]:
        print(choice)
    user_answer = int(input("Enter your Answer (1-4): "))
    
    if user_answer == q["correct"]:
        print(f"Yes! Correct Answer is: {q['choices'][q['correct']-1].split(': ')[1]}")
        print(f"You won Rs.{q['prize']}")
        total_prize += q["prize"]
    else:
        print(f"No! Wrong Answer. The correct answer is: {q['choices'][q['correct']-1].split(': ')[1]}")
        break

print(f"\nGame Over! You are taking home Rs.{total_prize}")