import random

# Define a function to generate a random greeting message
def greeting():
  messages = ["Hi there!", "Hello!", "Hey!"]
  return random.choice(messages)

# Define a function to respond to user input
def respond(input_text):
  # List of possible user inputs and corresponding responses
  user_inputs = {
      "hi": "Hi there!",
      "hello": "Hello!",
      "how are you": "I'm doing well, thank you for asking!",
      "bye": "Goodbye!",
      "": "Sorry, I didn't understand that."
  }
  
  # Check if user input matches any of the keys in user_inputs dictionary
  if input_text.lower() in user_inputs:
    return user_inputs[input_text.lower()]
  else:
    return "Sorry, I don't understand that."

# Define the main function to run the chatbot
def main():
  print("Chatbot: " + greeting())
  
  # Keep the chatbot running until the user enters "bye"
  while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
      print("Chatbot: " + respond(user_input.lower()))
      break
    else:
      print("Chatbot: " + respond(user_input.lower()))

# Run the main function to start the chatbot
if __name__ == "__main__":
  main()
