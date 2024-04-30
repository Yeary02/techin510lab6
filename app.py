import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def send_prompt(prompt_text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Direct Request
direct_request = "Describe how a Large Language Model works."
print("Direct Request Answer:", send_prompt(direct_request))

# Few-shot Example
few_shot_example = """Q: Explain the concept of gravity.
A: Gravity is the force that attracts two bodies towards each other, typically observed between objects with mass. It's why we stay grounded on Earth and why planets orbit the sun.

Q: What is machine learning?
A: """
print("Few-shot Example Response:", send_prompt(few_shot_example))

# Zero-shot Approach
zero_shot_approach = "Compose a poem about the sea."
print("Zero-shot Approach Response:", send_prompt(zero_shot_approach))
