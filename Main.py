from WhatsappClass import WhatsappBot


def main():
    message = str(input("Mensagem a ser enviada: "))
    groups = []
    loop = True

    while loop:
        to_group = str(input("Grupo de destino (enter para finalizar): "))

        if not to_group:
            loop = False
        else:
            groups.append(toGroup)

    bot = WhatsappBot(message, groups)
    bot.send_messages()


if __name__ == '__main__':
    main()
