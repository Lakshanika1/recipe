import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_recipe(user_input):
    system_prompt = """
You are a recipe generator AI.

Rules:
1. Only generate recipes.
2. If the user input is NOT a list of food ingredients, respond with:
   "I can only generate recipes from ingredients provided."
3. Output format must be strictly:

Dish Name: <name>

Ingredients Required:
- item 1
- item 2

Steps:
1. Step one
2. Step two
"""

    full_prompt = system_prompt + "\nUser Input:\n" + user_input
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=full_prompt
    )
    return response.text
while True:
    user_input = input("Enter ingredients (or type 'exit'): ")
    if user_input.lower() == "exit":
        break
    output = generate_recipe(user_input)
    print("\n", output)