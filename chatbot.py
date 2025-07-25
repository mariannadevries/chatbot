import random
import re

# ----------------------------
# 1. Predefined Responses
# ----------------------------
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi, how can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "default": ["I'm not sure I understand.", "Could you rephrase that?", "Interesting... tell me more."]
}

# ----------------------------
# 2. Intent Detection
# ----------------------------
def get_intent(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "greeting"
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "goodbye"
    elif re.search(r"\b(thank|thanks)\b", user_input):
        return "thanks"
    else:
        return "default"

# ----------------------------
# 3. Chatbot Response
# ----------------------------
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# ----------------------------
# 4. Run Chatbot
# ----------------------------
def run_chatbot():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    run_chatbot()
