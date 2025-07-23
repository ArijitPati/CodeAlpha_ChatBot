# Pre-set response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "My name is ChatBox."
    elif user_input == "who made you":
        return "I'm made by Arijit Pati!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

# Chat loop
print("Chatbot: Hello! Type something (type 'bye' to exit).")
while True:
    user = input("You: ")
    response = chatbot_response(user)
    print("Chatbot:", response)
    
    if user.lower() == "bye":
        break