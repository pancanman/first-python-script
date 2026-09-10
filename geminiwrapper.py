import os
import dotenv
from google import genai
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

load_dotenv()
api = os.getenv("GEMINI_API_1")

client = genai.Client(api_key=api)

modelchoice = input("Type a model (ex gemini-3.1-flash-lite): gemini-")

chat = client.chats.create(model=f"gemini-{modelchoice}")

with open("memory.txt", "w", encoding="utf-8") as file:
    file.write("New Chat")

while True:
    prompt = input("Chat: ")

    if prompt == "quit":
        break
    if prompt == "wipedata":
        with open("memory.txt", "w", encoding="utf-8") as file:
            file.write("")
        continue
    if prompt == "switchmodel":
        switchprompt = input("Type a new model (ex gemini-3.1-flash-lite): gemini-")
        chat = client.chats.create(model=f"gemini-{switchprompt}")
        continue
    if prompt == "help":
        print("\nHelp\n----\n\nquit: Exit the chat\nwipedata: Wipe the memory.txt file\nswitchmodel: Switch the model of the chat")
        continue
    
    print("Gemini is thinking...")
    response = chat.send_message(prompt)

    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    print(f"({formatted}) API: {response.text}")

    with open("memory.txt", "a", encoding="utf-8") as file:
        file.write(f"\n\n({formatted})\n\nUser: {prompt}\n\nAPI: {response.text}")
