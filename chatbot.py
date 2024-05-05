from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

#Removendo alertas de campo em branco
logging.basicConfig(level=logging.CRITICAL)

# isso aqui só precisa para corrigir o bug
from spacy.cli import download

#Configurando os tipos de textos
chatbot = ChatBot("botIa", tagger_language=download("en_core_web_sm"))

#Váriaveis de resposta na ordem das perguntas
conversa = [
    "Olá, como posso ajuda-lo ?",
    "Qual o horário de funcionamento ?",
    "Estamos disponíveis de segunda a sexta dás 8h ás 18h e dás 8h ás 13h nos feriados e finais de semana",
    "Quais são os carros disponíveis ?",
    "Possuimos Fiat Uno, Volkswagen Gol, Chevrolet Onix, Toyota Corolla, Hyundai Elantra, Volkswagen Jetta, Audi A8 e muitos outros, que tal vim conhecer nossa concessionária ? Fica na rua x número y",
    "Obrigado pela ajuda",
    "De nada ^^, qualquer coisa estamos a disposição",
]

#Iniciando o treinamento e salvando as variações de diálogo
trainer = ListTrainer(chatbot)
trainer.train(conversa)

#Teste do chat
while True:
    mensagem = input("Mande uma mensagem para o chatbot:")
    if mensagem == "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)