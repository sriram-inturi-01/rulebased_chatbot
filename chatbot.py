import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I help you today?"

    # Asking about chatbot
    elif re.search(r"\b(who are you|what are you)\b", user_input):
        return "I’m a simple rule-based chatbot created to help you."

    # Asking about weather
    elif re.search(r"\b(weather|temperature)\b", user_input):
        return "I can't check live weather yet, but it's always sunny in my world!"

    # Asking about time
    elif re.search(r"\b(time|clock)\b", user_input):
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    # Asking about creator
    elif re.search(r"\b(who made you|your creator|developer)\b", user_input):
        return "I was created by a developer learning about chatbots."

    # Goodbye
    elif re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Sorry, I don't understand that yet. Can you rephrase?"

# Chat loop
print("🤖 Chatbot is running! Type 'quit' to exit.")
while True:
    user_text = input("You: ")
    if user_text.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break
    response = chatbot_response(user_text)
    print("Chatbot:", response)
