import random

# Define a list of greetings and responses
greetings = ["hello", "hi", "hey", "howdy"]
responses = ["Hello!", "Hi there!", "Hey!", "How can I help you today?"]

# Function to generate a response
def respond_to_greeting(user_greeting):
    user_greeting = user_greeting.lower()
    
    for word in greetings:
        if word in user_greeting:
            return random.choice(responses)
    
    return "I'm not sure how to respond to that."

# Main loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = respond_to_greeting(user_input)
    print("AI: " + response)
