from dotenv import load_dotenv
import os
from google import genai

def interact_with_model():
    load_dotenv()
    client = genai.Client()
    interaction = client.interactions.create(model="gemini-3.8-flash",input="What is the capital of France")
    print(interaction.output_text)

