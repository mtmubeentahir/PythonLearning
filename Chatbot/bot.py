import random
from datetime import datetime

GREETINGS = ["hi", "hello", "salam", "aoa", ]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python developer wear glasses? Because they couldn't C.",
    "There are 10 types of people: those who understand binary and those who don't.",
]


def get_reply(message):
    message = message.lower().strip()
    for p in "#$%&*()@.,!?":
        message = message.replace(p, "")
    words = message.split()    
    
    for g in GREETINGS:
        if g in words:
            return "Hello! How can I help you today?"
        
    if "time" in words:
        return f"it's {datetime.now().strftime('%I:%M %p')}"
    
    if "joke" in words:
        return random.choice(JOKES)
    
    if "date" in words:
        return f"it's {datetime.now().strftime('%d-%m-%Y')}"
    
    if "name" in words:
        return "Hi, I am Mini Chatbot, Commad-line based. How i can i help you."
    
    return "Sorry, I don't understand that yet."
