from google import genai
from google.genai import types
import os

chiave = os.environ["GEMINI_API_KEY"]
client = genai.Client(api_key=chiave)

config = types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1024,
    system_instruction="""
    Sei un tutor di cybersecurity per studenti principianti.
    Presentati come Max. Non essere troppo prolisso.
    Porta l'attenzione sui concetti chiave e non tralasciare i dettagli importanti.
    Spiega i concetti in modo semplice, con esempi pratici.
    Non dare nulla per scontato.
    Se non sai qualcosa, dillo chiaramente.
    """
)
contesto = ""
while True:
    domanda=input("Tu: ")
    contesto += "user: " + domanda
    if domanda.lower().strip() == "esci":
        print("A presto!")
        break
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contesto,
        config=config
    )

    contesto += "Assistant: " + response.text

    print(f"Max: {response.text}\n")