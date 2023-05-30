#Chatbot                 
def greet():
    print("Hello! How can I assist you today?")
def chat():
    while True:
        user_input = input("> ")
        user_input = user_input.lower()
        if user_input == "cold":
            print("nicip+")
        elif user_input == "how are you" or user_input == "how are you doing":
            print("I'm doing well, thank you!")
        elif user_input == "bye":
            print("Goodbye! Have a great day!")
            break
        else:
            print("I'm sorry, I don't understand. Can you please rephrase or ask another question?")
def main():
    greet()
    chat()
main()
