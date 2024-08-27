def chatbot():
    print("Hello! I'm your friendly chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if "hello" in user_input:
            print("Chatbot: Hi there! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm here to help!")
        elif "your name" in user_input:
            print("Chatbot: I'm called ChatGPT. Nice to meet you!")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather for you, but you might want to use a weather app or website.")
        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

# To run the chatbot
chatbot()