# Interactive conversation with Python using strings

print("Welcome to the Python chat! 🌟")
print("You will talk to ChatBot. Type 'bye' to end the conversation.\n")

while True:
    # Get user input
    user_input = input("You: ")
    
    # Convert to lowercase to make comparisons easier
    user_input_lower = user_input.lower()
    
    # Exit condition
    if user_input_lower == "bye":
        print("ChatBot: Goodbye! It was nice talking to you! 👋")
        break
    # Simple responses
    elif "hello" in user_input_lower or "hi" in user_input_lower:
        print("ChatBot: Hi there! How are you today? 😊")
    elif "how are you" in user_input_lower:
        print("ChatBot: I'm just a program, but I'm feeling great! How about you?")
    elif "python" in user_input_lower:
        print("ChatBot: Python is amazing! Do you like coding in Python? 🐍")
    elif "yes" in user_input_lower:
        print("ChatBot: That's awesome! Keep coding and have fun! ✨")
    elif "no" in user_input_lower:
        print("ChatBot: No worries! Everyone starts somewhere. You can learn it gradually! 💡")
    else:
        print("ChatBot: Hmm, I didn't understand that. Can you say it differently? 🤔")
