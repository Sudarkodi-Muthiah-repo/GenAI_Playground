from anthropic import Anthropic
from dotenv import load_dotenv
import os

def interact_with_model():
    load_dotenv()
    client = Anthropic()
    #client = Anthropic(api_key = os.getenv('ANTHROPIC_API_KEY'))
    message =client.messages.create(
        max_tokens=50,messages=[{"role": "user", "content": "What is the capital of France?"}],model="claude-haiku-4-5"
    )

    #for block in message.content:
        #if block.type == "text":
        #    print(block.text)

    print(message)