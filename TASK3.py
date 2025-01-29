import random

def chatbot():
    print("Hello! I'm your friendly chatbot. How can I assist you today?")
    print("Type 'bye' to end the conversation.")

    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but I'm here to assist you! How can I help?",
        "what is your name": "I'm Chatbot! What's your name?",
        "bye": "Goodbye! Have a great day!",
        "what can you do": "I can chat with you, answer basic questions, and try to help you feel better!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is python": "Python is a powerful, easy-to-learn programming language used for web development, data analysis, AI, and more.",
        "what is the weather like": "I'm not sure, but I hope it's nice outside!",
        "tell me a fun fact": "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
        "who created you": "I was created by programmers to assist with conversations and tasks!"
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: " + responses["bye"])
            break

        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        print("Chatbot: " + response)

if __name__ == "__main__":
    chatbot()