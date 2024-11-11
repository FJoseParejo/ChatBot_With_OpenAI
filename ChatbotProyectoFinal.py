import openai
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env mediante dotoenv
load_dotenv()

# Accedemos a las variables de entorno mediante fichero .env para reforzar la seguridad de los datos 
openai.api_key = os.getenv('SECRET_KEY')

def chat_with_openai():
    print("Chatbot: Hola, ¿Cómo puedo ayudarte hoy? (Escribe 'salir' para finalizar)")

    request_count = 0

    while True:
        user_input = input("Tú: ")

        if user_input.lower() == 'salir':
            print("Chatbot: ¡Adiós!")
            break

        try:
            # Usa ChatCompletion con `gpt-3.5-turbo`
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "Proporciona respuestas completas y detalladas."},
            {"role": "user", "content": user_input}
            ],
            max_tokens=100,
            temperature=0.9
)

            request_count += 1
            print(f"Solicitudes realizadas: {request_count}")

            answer = response.choices[0].message['content'].strip()
            print(f"Chatbot: {answer}")
            
        except Exception as e:
            print(f"Error: {e}")

# Inicia el chat
chat_with_openai()
