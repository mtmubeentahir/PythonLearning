# Python Learning Journey 🐍

My step-by-step journey learning Python from scratch, on my way

Each `PracticeN.py` file contains my solutions to the exercises for one lesson. The `Chatbot/` folder is the final mini project that brings everything together.

## 📚 Lessons

| # | Topic | File |
|---|---|---|
| 1 | `print()`, variables, data types, f-strings | [Practice1.py](Practice1.py) |
| 2 | Input, type conversion, operators | [Practice2.py](Practice2.py) |
| 3 | Strings and string methods | [Practice3.py](Practice3.py) |
| 4 | Conditions (`if` / `elif` / `else`) | [Practice4.py](Practice4.py) |
| 5 | Loops (`for`, `while`, `break`, `continue`) | [Practice5.py](Practice5.py) |
| 6 | Lists and tuples | [Practice6.py](Practice6.py) |
| 7 | Dictionaries and sets | [Practice7.py](Practice7.py) |
| 8 | Functions | [Practice8.py](Practice8.py) |
| 9 | Error handling (`try` / `except`) | [Practice9.py](Practice9.py) |
| 10 | Files and JSON | [Practice10.py](Practice10.py) |
| 11 | Modules, pip, virtual environments | [Practice11.py](Practice11.py), [helper.py](helper.py) |
| 12 | Classes and objects (OOP) | [Practice12.py](Practice12.py) |
| 13 | Mini project: command-line chatbot | [Chatbot/](Chatbot/) |

## 🤖 Project: Command-Line Chatbot

A simple chatbot that runs in the terminal. It replies to greetings, tells jokes, gives the time and date, and remembers the conversation between runs.

**Structure**

```
Chatbot/
├── main.py           # chat loop and commands
├── bot.py            # get_reply(): the bot's "brain"
└── conversation.py   # Conversation class: stores, saves and loads messages
```

**Commands**

| Command | What it does |
|---|---|
| `/help` | list all commands |
| `/history` | show the conversation, numbered |
| `/stats` | count user and bot messages |
| `/search word` | show messages containing a word |
| `/save` | save the chat under a custom file name |
| `/clear` | empty the conversation |
| `/quit` | save the chat and exit |

**Run it**

```bash
cd Chatbot
python main.py
```

The chat is saved to `chat_history.json` and loaded automatically the next time you start the bot.

**Concepts used:** classes, modules, JSON files, error handling, dictionaries, loops, `random` and `datetime`.

## ▶️ Running the practice files

Requires **Python 3**. No external packages are needed.

```bash
python Practice5.py
```

Most files ask for input, and each one runs all of its lesson's exercises in order.

## 👤 Author

**Mubeen Tahir** · [GitHub](https://github.com/mtmubeentahir)
