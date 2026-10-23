# =====================================================================
#  MINI Chatbot - Command Line Base
# =====================================================================
import json
from typing import Literal

class Conversation:
    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []
        
    def add_message(self, role: Literal["user", "assistant"], message: str, time: str) -> None:
        if role not in ("user", "assistant"):
            print(f"Error: invalid role '{role}'")
            return
        self.messages.append({"role": role, "text": message, "time":  time})
    
    def show(self)-> None:
        for index, msg in enumerate(self.messages, start=1):
            print(f"{index} - Time: {msg['time']} - {msg['role']}: {msg['text']}")
            
    def save(self, filename: str)-> None:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4)
    
    def load(self, filename: str)-> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.messages = json.load(file)
        except FileNotFoundError:
            return