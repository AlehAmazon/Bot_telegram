import telebot


CHAVE_API="162282715:AAF3qxDBCLv2qh68d1Xi1QjVAvWe4sciK3E"
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

def verificar(menagem):
    return True

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Bot criado para passar informações utéis sobre o atendimento. Escolha entre os comandos validos digitando '/' . Ainda em fase de testes.")
    

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
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
    arquivo = open("documentos/cartaosus.txt",'r')
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

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    pass

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    pass

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


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''
    Escolha uma opção para continuar (Clique no item):
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraço
    Responder qualquer outra coisa não irá funcionar, clique em uma das opções    '''
    bot.reply_to(mensagem, texto)


#----------------------------MAIN------------------------------------
def main ():	
    linha()

    # Start the Bot
    bot.polling ()
    bot.idle()




print ("Getting updates".center(50, '-'))
print ("")
print ("Iniciando o BotUBSDrLM...")
print ("Versão 1.0.11.1")


'''
======================================================================
INICO DO PROGRAMA
======================================================================
'''

if __name__ == '__main__':
    main()