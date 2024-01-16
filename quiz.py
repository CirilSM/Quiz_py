# Quiz Questions and Answers
quiz_data = {
    "Cyber Security": [
        {"question": "What does VPN stand for?", "options": ["Virtual Private Network", "Very Personal Network", "Virtual Public Network", "Visual Private Network"], "answer": "Virtual Private Network"},
        {"question": "Which of the following is a strong password?", "options": ["password", "P@ssw0rd", "123456", "qwerty"], "answer": "P@ssw0rd"},
        {"question": "What is the purpose of a firewall?", "options": ["Protects against viruses", "Monitors internet speed", "Controls network access", "Manages computer files"], "answer": "Controls network access"},
        {"question": "What is phishing?", "options": ["Fishing in the sea", "A cyber attack to steal information", "A programming language", "A type of computer virus"], "answer": "A cyber attack to steal information"}
    ],
    "Mathematics": [
        {"question": "What is the value of pi (π)?", "options": ["3.14", "2.71", "1.618", "4.20"], "answer": "3.14"},
        {"question": "Solve for x: 2x + 5 = 15", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"question": "What is the square root of 64?", "options": ["6", "8", "10", "12"], "answer": "8"},
        {"question": "In a right-angled triangle, what is the length of the hypotenuse if the other sides are 3 and 4?", "options": ["5", "6", "7", "8"], "answer": "5"}
    ],
    "Simple Coding": [
        {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "High-level Text Machine Language", "HyperText and links Markup Language", "Home Tool Markup Language"], "answer": "HyperText Markup Language"},
        {"question": "Which programming language is known for its simplicity and readability?", "options": ["C++", "Python", "Java", "Ruby"], "answer": "Python"},
        {"question": "What is the result of 2 + 3 * 4?", "options": ["14", "20", "24", "32"], "answer": "14"},
        {"question": "In Python, how do you comment a single line of code?", "options": ["//", "#", "--", "/* */"], "answer": "#"}
    ],
    "Riddles": [
        {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "options": ["Echo", "Whistle", "Ghost", "Windmill"], "answer": "Echo"},
        {"question": "The more you take, the more you leave behind. What am I?", "options": ["Footsteps", "Money", "Memories", "Time"], "answer": "Footsteps"},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "options": ["The letter M", "The number 2", "The word 'now'", "The letter A"], "answer": "The letter M"},
        {"question": "What has keys but can't open locks?", "options": ["Keyboard", "Piano", "Treasure chest", "Map"], "answer": "Piano"}
    ],
    "Big Data": [
        {"question": "What is the term used to describe the massive volume of structured and unstructured data that is generated and processed by organizations?", 
         "options": ["Large Data", "Huge Data", "Big Data", "Massive Data"], 
         "answer": "Big Data"},
        {"question": "Which programming language is commonly used for processing and analyzing Big Data?", 
         "options": ["Java", "Python", "C#", "R"], 
         "answer": "Java"},
        {"question": "What is Hadoop?", 
         "options": ["A programming language", "A big data processing framework", "A data storage device", "A machine learning algorithm"], 
         "answer": "A big data processing framework"},
        {"question": "What is the purpose of Apache Spark in the context of Big Data?", 
         "options": ["Data visualization", "Data storage", "Data processing", "Data encryption"], 
         "answer": "Data processing"}
    ]
}

def run_quiz(topic):
    questions = quiz_data.get(topic, [])
    if not questions:
        print("Invalid topic.")
        return

    score = 0
    user_answers = {}

    print(f"\n--- {topic} Quiz ---\n")

    for i, question_data in enumerate(questions, start=1):
        question = question_data["question"]
        options = question_data["options"]
        answer = question_data["answer"]

        print(f"Q{i}. {question}")
        for j, option in enumerate(options, start=1):
            print(f"   {j}. {option}")

        user_input = input("Your Answer (1-4): ")

        try:
            user_answer_index = int(user_input) - 1
            user_choice = options[user_answer_index]
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")
            continue

        user_answers[question] = user_choice 

        if user_choice == answer:
            print("Correct! +5 marks\n")
            score += 5
        else:
            print(f"Wrong! The correct answer is: {answer}. -1 mark\n")
            score -= 1

    print(f"\nYour {topic} Quiz Score: {score} marks\n")

    if score < len(questions):
        print("Incorrect Choices:")
        for question, user_choice in user_answers.items():
            correct_answer = next(q["answer"] for q in questions if q["question"] == question)
            if user_choice != correct_answer:
                print(f"Q: {question}\nYour Answer: {user_choice}\nCorrect Answer: {correct_answer}\n")

if __name__ == "__main__":
    while True:
        print("\n--- Choose a Quiz Topic ---")
        for i, topic in enumerate(quiz_data.keys(), start=1):
            print(f"{i}. {topic}")

        print("0. Exit")
        choice = input("Enter your choice (0-5): ")

        if choice == "0":
            print("Thank you for taking the quiz! Goodbye.")
            break

        try:
            choice_index = int(choice) - 1
            selected_topic = list(quiz_data.keys())[choice_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        run_quiz(selected_topic)

        play_again = input("Do you want to try another quiz? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for taking the quiz! Goodbye.")
            break
