# =====================================================================
#  MINI Chatbot - Command Line Base
# =====================================================================
import json
from typing import Literal
from pydantic import BaseModel

class Message(BaseModel):
    role: Literal["user", "assistant"]
    text: str
    time: str
    
    

class Conversation:
    def __init__(self) -> None:
        self.messages: list[Message] = []
        
    def add_message(self, role: Literal["user", "assistant"], message: str, time: str) -> None:
        self.messages.append(Message(role= role, text= message, time=  time))
    
    def show(self)-> None:
        for index, msg in enumerate(self.messages, start=1):
            print(f"{index} - Time: {msg.time} - {msg.role}: {msg.text}")
            
    def save(self, filename: str)-> None:
        data = [ msg.model_dump() for msg in self.messages ]
            
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    
    def load(self, filename: str)-> None:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                msgs = json.load(file)

            self.messages = [Message.model_validate(ms) for ms in msgs ]
        except FileNotFoundError:
            return