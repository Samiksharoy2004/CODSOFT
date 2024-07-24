import random

rules = {
    'hello': 'Hi! How can I assist you today?',
    'hi': 'Hello! What brings you here?',
    'how are you': 'I am doing great, thanks for asking!',
    'what is your purpose': 'I am here to assist you with any questions or concerns you may have.',
    'exit': 'Goodbye! It was nice chatting with you.'
}

def process_input(user_input):
    user_input = user_input.lower()
    if user_input in rules:
        return rules[user_input]
    elif 'help' in user_input:
        return 'I can assist you with basic queries. Type "hello" to get started.'
    else:
        return 'Sorry, I did not understand that. Please try again.'

def start_chatbot():
    print('Welcome to the chatbot!')
    while True:
        user_input = input('You: ')
        response = process_input(user_input)
        print('Chatbot: ', response)
        if user_input.lower() == 'exit':
            break

start_chatbot()
