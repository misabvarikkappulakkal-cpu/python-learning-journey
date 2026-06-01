from questions import questions


def run_quiz():
    score = 0

    print("\n===== PYTHON QUIZ =====\n")

    for index, q in enumerate(questions, start=1):

        print(f"Question {index}")
        print(q["question"])

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer: ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(
                f"❌ Wrong! Correct answer: {q['answer']}\n")

    print("=" * 30)
    print(f"Final Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100

    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("🏆 Excellent!")

    elif percentage >= 50:
        print("👍 Good Job!")

    else:
        print("📚 Keep Practicing!")


run_quiz()