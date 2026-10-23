# =====================================================================
#  MINI Chatbot - Command Line Base
# =====================================================================
import json

class Conversation:
    def __init__(self):
        self.messages = []
        
    def add_message(self, role, message, time):
        if role not in ("user", "assistant"):
            print(f"Error: invalid role '{role}'")
            return
        self.messages.append({"role": role, "text": message, "time":  time})
    
    def show(self):
        for index, msg in enumerate(self.messages, start=1):
            print(f"{index} - Time: {msg['time']} - {msg['role']}: {msg['text']}")
            
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4)
    
    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            return