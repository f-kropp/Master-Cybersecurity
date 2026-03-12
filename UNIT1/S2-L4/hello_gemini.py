from google import genai
from google.genai import types
import os

chiave = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=chiave)

config = types.GenerateContentConfig(
    temperature=0.9,
    max_output_tokens=1024,
    system_instruction="""
    Sei un assistente amichevole per studenti di programmazione.
    Rispondi in modo semplice e chiaro.
    Non dare per scontato e approfondisci. 
    """
)

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Ciao! Chi sei?", 
    config=config
)

print(response.text)