import re

def rule_based_chatbot(input_text):
    # Define rules for responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a chatbot. I don\'t have feelings, but thanks for asking!',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'what is your name': 'I am a rule-based chatbot.',
        r'(\w+) weather': 'I\'m sorry, I cannot provide real-time weather information.',
        r'default': 'I\'m not sure how to respond to that.'
    }

    # Check input against rules
    for pattern, response in rules.items():
        if re.search(pattern, input_text, re.IGNORECASE):
            return response

    # If no match found, use the default response
    return rules['default']

# Main loop for interacting with the chatbot
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    # Get the chatbot's response based on rules
    bot_response = rule_based_chatbot(user_input)
    print("Chatbot:", bot_response)