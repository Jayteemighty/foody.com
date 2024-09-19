import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_food_related_question(question: str) -> str:
    prompt = f"You're an expert chef. Only answer questions about food and cooking. {question}"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another model you want to use
            prompt=prompt,
            max_tokens=150,  # Limit the response length
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Extract the generated text from the response
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"
