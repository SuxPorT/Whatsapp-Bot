from selenium import webdriver
import time


class WhatsappBot():

    def __init__(self, message, groups):
        """ Construtor da classe
        
        Keyword arguments:
        message -- mensagem a ser enviada
        groups -- grupos à que a mensagem será enviada
        """
        self.message = message
        self.groups = groups
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")

    def send_messages(self):
        """ Função que irá acionar as mensagens, sendo composta de três elementos HTML:
        1. Span do título do grupo
        2. Div da caixa de texto da mensagem
        3. Span do botão de envio da mensagem
        """
        self.driver.get("https://web.whatsapp.com/")

        # Espera para fazer a autenticação
        time.sleep(30)

        for group in self.groups:
             # Span do HTML indicando o título do grupo
            group = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
            time.sleep(3)
            group.click()

            # Div do HTML indicando a caixa de texto da mensagem
            chat_box = self.driver.find_element_by_class_name("_3uMse")
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)

            # Span do HTML indicando o botão de envio da mensagem
            send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            send_button.click()
            time.sleep(5)
