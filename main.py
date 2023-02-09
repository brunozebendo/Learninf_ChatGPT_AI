"""A intenção do código é criar um aplicativo simples com uma caixa de diálogo com o
chatGPT, usando a API dele para isso"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading

"""aqui a classe que vai gerar a janela que vai incorporar os widgets de diálogo"""


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Instanciando o chatbot e o transformando em um atributo
        self.chatbot = Chatbot()


        self.setMinimumSize(700, 500)

        # Área do widget de chat
        """o atributo self relaciona o widget abaixo com o de cima, que é o da janela principal"""
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)

        # Área do input
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(15, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # adicionando botão
        """o click.connect vai fazer a ligação entre o que o usuário digitar o chat assim que o botão for clicado"""
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

        """o código abaixo vai capturar o que for digitado na área do input e acrescentar (append) no espaço
        do chat e depois limpar o input"""
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()
        """o código estava lançando o pergunta junto com a resposta na área do chat, para
        evitar isso foi criado código abaixo, para que ele trate diferente a função get_bot_reponse"""
        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()
        """abaixo o código para incluir a resposta no área do chat"""
    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333'; background-color: #E9E9E9'>Bot: {response}</p>")



app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
