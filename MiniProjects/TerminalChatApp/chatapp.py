responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there!",
    "how are you": "I'm doing great. Thanks for asking!",
    "bye": "Goodbye!",
    "python": "Python is a powerful programming language.",
    "github": "GitHub is a platform for version control and collaboration."
}

print("=== Terminal Chat App ===")
print("Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in ["exit", "bye"]:
        print("Bot: Goodbye!")
        break

    response = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", response)