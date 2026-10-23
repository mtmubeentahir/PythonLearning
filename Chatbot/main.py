from bot import get_reply
from conversation import Conversation
from datetime import datetime
COMMANDS = {
    "/help": "lists all commands",
    "/history": "shows the conversation, numbered",
    "/stats": "shows how many messages the user and the bot have sent",
    "/clear": "empties the conversation",
    "/quit": "saves the chat and exits",
    "/save": "saves the chat to a file with a custom name.",
    "/search": "/search word shows only the messages containing that word."
    }
chat_history = Conversation()
chat_history.load("chat_history.json")
length = len(chat_history.messages)
if length > 0:
    print(f"Loaded {length} previous messages")

while True:
    message = input("You: ").strip()
    if message == "":
        continue
    if message.startswith('/search '):
        word = message.split()[1].lower()
        for msg in chat_history.messages:
            if word in msg["text"].lower():
                print(f"{msg['role']}: {msg['text']}")
        continue

    if message.startswith('/'):
        if message in COMMANDS:
            if message == "/help":
                print("These are available commands:")
                for comand, action in COMMANDS.items():
                    print(f"{comand}    {action}")
            elif message == "/history":
                chat_history.show()
            elif message == "/stats":
                user_count = 0
                bot_count = 0
                for msg in chat_history.messages:
                    if msg["role"] == "user":
                        user_count += 1
                    else:
                        bot_count += 1
                print(f"Total user messages: {user_count} messages")
                print(f"Total Bot messages: {bot_count} messages")
            elif message == "/clear":
                chat_history.messages = []
                chat_history.save("chat_history.json")
                print("Chat cleared.")
            elif message == "/save":
                file_name = input("Enter filename with without extension: ").strip().lower()
                chat_history.save(f"{file_name}.json")
                print(f"Chat is saved with filename: {file_name}")
            elif message == "/quit":
                chat_history.save('chat_history.json')
                print("Chat saved, Goodbye!")
                break
        else:
            print("Unknown command. Type /help.")
        continue
    
    chat_history.add_message("user", message, datetime.now().strftime('%I:%M'))
    reply = get_reply(message)
    chat_history.add_message("assistant", reply, datetime.now().strftime('%I:%M'))
    print(f"Bot: {reply}")    

