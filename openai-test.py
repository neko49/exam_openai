import os
from openai import OpenAI, OpenAIError

# Récupérer la clé API à partir de la variable d'environnement
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
# Vérifier si la clé API a été correctement récupérée
if api_key is None:
    raise ValueError("OPENAI_API_KEY n'est pas défini dans les variables d'environnement.")

# Créer une instance du client OpenAI avec la clé API
client = OpenAI(api_key=api_key)

# Demander à l'utilisateur de saisir une question
question = input("Posez-moi une question sur la gestion du stress : ")

try:
    # Envoi de la question à l'API de ChatGPT
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Bonjour, je suis un assistant pour le développement personnel. Posez-moi des questions sur la gestion du stress, l'amélioration de la productivité ou le développement personnel."},
            {"role": "user", "content": question}
        ]
    )

    # Afficher la réponse obtenue à l'utilisateur
    response = completion.choices[0].message
    print(response.content)

except OpenAIError as e:
    # Gérer les erreurs de requête
    print(f"Une erreur s'est produite : {e}")
