from chatterbot import ChatBot # Importa la clase ChatBot

# Definimos chatbot pasando como argumento el nombre que le daremos al Bot

# También indicaremos los parámetros de entrenamiento del bot

chatbot = ChatBot(

    'EjemploBot',

    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'

)



# Entrenamos al bot en el idioma que necesitemos

# Los idiomas disponibles se encuentran en la documentación

# Solo es necesario ejecutar el entrenamiento una vez



chatbot.train("chatterbot.corpus.spanish")

# Ejemplo de conversación

while True:

    usuario = input(">>> ")

respuesta = chatbot.get_response(usuario)

print ("bot: "+str(respuesta))
