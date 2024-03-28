import tkinter as tk
from questionChatBot import ask_question

def send_question():
    """
    Fonction pour envoyer la question saisie par l'utilisateur et afficher la réponse du chatbot.
    """
    question = entry.get()  # Récupérer la question saisie par l'utilisateur depuis la zone de texte
    response = ask_question(question)  # Poser la question au chatbot et récupérer la réponse
    output.insert(tk.END, response + "\n")  # Afficher la réponse dans la zone de texte

def quit_program():
    """
    Fonction pour quitter le programme.
    """
    root.quit()

root = tk.Tk()
root.title("Chatbot pour la gestion du stress")

label = tk.Label(root, text="Posez une question sur la gestion du stress :")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Envoyer", command=send_question)
button.pack()

quit_button = tk.Button(root, text="Quitter", command=quit_program)
quit_button.pack()

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()
