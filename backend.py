import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"
    """o código abaixo são as configurações para user a API, o tipo de engenharia, o tipo de entrada e
    o máximo de caracteres na resposta, temperatura tem a ver com a precisão da resposta"""
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("what is the earth circunference?")
    print(response)