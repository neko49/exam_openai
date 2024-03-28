import os
from openai import OpenAI, OpenAIError

def ask_question(question):
    """
    Fonction pour poser une question à l'API de ChatGPT et obtenir une réponse.
    """
    # Récupérer la clé API à partir de la variable d'environnement
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Vérifier si la clé API a été correctement récupérée
    if api_key is None:
        raise ValueError("OPENAI_API_KEY n'est pas défini dans les variables d'environnement.")

    # Créer une instance du client OpenAI avec la clé API
    client = OpenAI(api_key=api_key)

    try:
        # Envoi de la question à l'API de ChatGPT
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Bonjour, je suis un assistant pour le développement personnel. Posez-moi des questions sur la gestion du stress, l'amélioration de la productivité ou le développement personnel."},
                {"role": "user", "content": question}
            ]
        )

        # Récupérer la réponse obtenue de l'API
        response = completion.choices[0].message.content
        return response

    except OpenAIError as e:
        # Gérer les erreurs de requête
        return f"Une erreur s'est produite : {e}"

# if __name__ == "__main__":
#     # Demander à l'utilisateur de saisir une question
#     question = input("Posez-moi une question sur la gestion du stress : ")
#     # Poser la question à l'API et afficher la réponse obtenue
#     print(ask_question(question))
