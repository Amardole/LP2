def simple_chatbot():
    print("Welcome to Simple Chatbot! (type 'exit' to quit)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hello! How can I help you?")
        elif user_input == "how are you":
            print("Bot: I'm doing well. Thank you!")
        elif user_input == "what is your name":
            print("Bot: I'm a basic chatbot.")
        elif user_input == "bye":
            print("Bot: Goodbye! Take care.")
            break
        elif user_input == "help":
            print("Bot: You can try saying 'hello', 'how are you', 'what is your name', or 'bye'.")
        else:
            print("Bot: Sorry, I don't understand that.")


simple_chatbot()
