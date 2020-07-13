import WhatsappClass

if __name__ == '__main__':
    message = str(input("Mensagem a ser enviada: "))
    groups = []
    loop = True

    while (loop):
        toGroup = str(input("Grupo de destino: "))

        if not toGroup:
            loop = False
        else:
            groups.append(toGroup)

    bot = WhatsappClass.WhatsappBot(message, groups)
    bot.SendMessages()
