def quiz_game():
    # Dictionary to store questions, options, and correct answers
    questions = {
        "What is the capital of France?": {
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Rome"],
            "answer": "A"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
            "answer": "C"
        },
        "Who wrote 'Hamlet'?": {
            "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) Mark Twain", "D) William Shakespeare"],
            "answer": "D"
        },
        "What is the largest ocean on Earth?": {
            "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
            "answer": "D"
        }
    }

    # Initialize score
    score = 0

    # Loop through each question
    for question, data in questions.items():
        print("\n" + question)
        for option in data["options"]:
            print(option)
        
        # Take user's answer
        user_answer = input("Your answer (A/B/C/D): ").upper()

        # Check if the answer is correct
        if user_answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {data['answer']}.")

    # Display final score
    print(f"\nQuiz Over! Your final score is {score}/{len(questions)}.")

# Call the function to start the quiz
quiz_game()
