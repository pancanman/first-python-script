import os
import dotenv
from google import genai
from dotenv import load_dotenv
from pathlib import Path
def clear():
    with open("memory.txt", "w", encoding="utf-8") as file:
        file.write("")
clear()
load_dotenv()
api = os.getenv("GEMINI_API_1")

client = genai.Client(api_key=api)

while True:
    prompt = input("Chat: ")
    if prompt == "quit":
        clear()
        break
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(f"API: {response.text}")

    with open("memory.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {prompt}")
        file.write(f"\nAPI: {response.text}")
