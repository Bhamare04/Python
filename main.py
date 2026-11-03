from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = "gemini-3.8-flash",
    contents="""
Explain deep learning to an MCA student who knows basic machine learning.
Use simple language.
Explain the difference between machine learning and deep learning.
Give one real-world example.
Keep the answer under 150 words.
"""
)
print(response.text)
