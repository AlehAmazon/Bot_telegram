__author__="AlehAmazon"

import telebot
import configparser
from telebot.types import Message


# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

CHAVE_API=(config['DEFAULT']['token'])
bot=telebot.TeleBot(CHAVE_API)

'''
=============================================================================
Funciona respondendo ao comandos digitados
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot
=============================================================================
'''


#Functions:

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Bot criado para passar informações utéis sobre o atendimento. Escolha entre os comandos validos digitando '/' . Ainda em fase de testes.")
    
@bot.message_handler(commands=['start'])
def handle_start_help(mensagem):
    # Handles
    texto = '''
    Escolha uma opção para continuar (Clique no item):
    /avisos Avisos e orientações
    /consultas Horários
    /cartaosus Cartão Nacional de Saúde
    /exames Informação sobre exames
    /sisreg Sistema de Regulação
    /telefone Telefones utéis
    Responder qualquer outra coisa não irá funcionar, clique em uma das opções    '''
    bot.reply_to(mensagem, texto)
    

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio', 'video','location','contact', 'voice', 'photo'] )
def handle_docs_audio(message):
	bot.send_message(message.chat.id, "Desculpe, Eu não conheço este comando.")

@bot.message_handler(commands=["avisos"])
def avisos(mensagem):
    arquivo = open("documentos/avisos.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["consultas"])
def consultas(mensagem):
    arquivo = open("documentos/consultas.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["cartaosus"])
def cartaosus(mensagem):
    arquivo = open("documentos/cns.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["exames"])
def exames(mensagem):
    arquivo = open("documentos/exames.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["sisreg"])
def sisreg(mensagem):
    arquivo = open("documentos/sisreg.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["telefone"])
def telefone(mensagem):
    arquivo = open("documentos/telefone.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["bolsafamilia"])
def bolsafamilia(mensagem):
    arquivo = open("documentos/bolsafamilia.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()    

@bot.message_handler(commands=["laboratorial"])
def laboratorial(mensagem):
    arquivo = open("documentos/laboratorial.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["testerapido"])
def testerapido(mensagem):
    arquivo = open("documentos/testerapido.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["preventivo"])
def preventivo(mensagem):
    arquivo = open("documentos/preventivo.txt",'r')
    conteudo = arquivo.read()
    bot.send_message(mensagem.chat.id,conteudo)
    arquivo.close()

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Valeu ! um abraço de volta")

def linha ():
    print ("")
    print ("Getting updates".center(50, '-'))
    print ("")
    print("Bot Ativo!")
    print ("")
    print ("Caso queira parar o Bot digite: Ctrl+C")
    print ("")
    print ("Getting updates".center(50, '-'))
    print ("")

def stop():
    bot.idle()
    bot.stop_bot(0)   

def verificar(menagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''
    Escolha uma opção para continuar (Clique no item):
    /avisos Avisos e orientações
    /consultas Horários
    /cartaosus Cartão Nacional de Saúde
    /exames Informação sobre exames
    /sisreg Sistema de Regulação
    /telefone Telefones utéis
    Responder qualquer outra coisa não irá funcionar, clique em uma das opções    '''
    bot.reply_to(mensagem, texto)


#----------------------------MAIN------------------------------------
def main ():	
    linha()
    
    #import tela

    # Start the Bot
    bot.polling ()

print ("Getting updates".center(50, '-'))
print ("")
print ("Iniciando o BotUBSDrLM...")
print ("Versão 1.0.11.3")


'''
======================================================================
======================================================================
'''
if __name__ == '__main__':
    main()