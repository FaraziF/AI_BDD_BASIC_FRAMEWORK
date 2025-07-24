from openai import OpenAI  # Import the OpenAI class for accessing the API
from config.prompts import prompts  # Import the prompts dictionary directly
import json


# Initialize the OpenAI client with the API key
def initialize_client():
    with open("config/openai_key.json", "r") as f:
        api_key = json.load(f)["api_key"]
    return OpenAI(api_key=api_key)


client = initialize_client()


def load_prompt(key):
    """Retrieve a prompt from the prompts dictionary."""
    return prompts.get(key, "")


# Generate text using OpenAI
def generate_text(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=messages,  # Pass the prompt message
        max_tokens=500,  # Limit the response to control length and cost
        temperature=0.1,  # Set a low temperature for more consistent outputs
        top_p=1.0,  # Consider all probable completions
    )
    return response.choices[0].message.content.strip()
