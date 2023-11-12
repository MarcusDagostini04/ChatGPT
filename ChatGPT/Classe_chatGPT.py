from Classe_ChromeDriver import *
import speech_recognition as sr
import requests
import json
import traceback
import pyttsx3
import time


class GPT:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = "gpt-3.5-turbo"
        self.link_para_modelos = "https://api.openai.com/v1/models/"
        self.link = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def obter_resposta(self, pergunta):
        body_mensagem = {
            "model": self.model,
            "messages": [{"role": "user", "content": pergunta}]
        }
        dados_msg = json.dumps(body_mensagem)

        try:
            print("Enviando sua pergunta aos nossos atendentes, 1 minuto por favor ...")
            requisicao_chat = requests.post(self.link, headers=self.headers, data=dados_msg)
            resposta = requisicao_chat.json()['choices'][0]['message']['content']
            return resposta
        except Exception as e:
            print(traceback.format_exc())
            return None
        
    def text_to_speech(self, texto):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        engine.say(texto)
        engine.runAndWait()

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Diga algo...")
                audio = recognizer.listen(source, timeout=5)
                print("Audio capturado.")
                time.sleep(0.4)
                print("Transcrevendo o audio, aguarde alguns segundos, por favor ...")
                texto = recognizer.recognize_google(audio, language='pt-BR')
                print("Pergunta transcrita.")
                print(linha())
                return texto 
        except sr.WaitTimeoutError:
            print("Não identificamos nenhuma fala")
            self.text_to_speech("Não identificamos nenhuma fala")
            print(linha())
            return self.speech_to_text()
        except sr.UnknownValueError:
            print("Não identificamos nenhuma fala")
            self.text_to_speech("Não identificamos nenhuma fala")
            print(linha())
            return self.speech_to_text()
    
    def opc_menu(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Sua resposta...")
                audio = recognizer.listen(source, timeout=5)
                print("Audio capturado.")
                time.sleep(0.4)
                print("Transcrevendo o audio, aguarde alguns segundos, por favor ...")
                texto = recognizer.recognize_google(audio, language='pt-BR')
                print("Audio transcrito.")
                print(linha())
                return texto 
        except sr.WaitTimeoutError:
            print("Não identificamos nenhuma fala")
            self.text_to_speech("Não identificamos nenhuma fala, digite a opção")
        except sr.UnknownValueError:
            print("Não identifivcamos nenhuma fala")
            self.text_to_speech("Não identificamos nenhuma fala, digite a opção")


site = "https://plusoft.com/contato/"

xpaths = [
    '//*[@id="menu_solucoes_rh"]',
    '//*[@id="menu_solucoes_marketing"]',
    '//*[@id="menu_solucoes_financeiro"]',
    '//*[@id="menu_solucoes_atendimentoaocliente"]',
    '//*[@id="menu_solucoes_ti"]'
]


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print("Usúario preferiu não digitar esse número.")
            return 0
        else:
            return n

def linha(tam=42):
    return'-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())

def exibir_menu(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        chatGPT.text_to_speech(f"{i} para, {opcao}")

def atendente_plusoft():
    cabeçalho('Pesquisar')
    while True:
        pergunta = input("Digite uma pergunta para o ChatGPT \nDigite 1 para sair \n")
        if pergunta == "1":
            print("Finalizando atendimento ...")
            break
        resp = chatGPT.obter_resposta(pergunta)
        print(f"Resposta: {resp}")

def atendente_por_voz():
    cabeçalho('Pesquisar por voz')
    chatGPT.text_to_speech("Pesquisar por voz")
    while True:
        print("Faça uma pergunta para o Atendente \nFale 'sair' para finalizar o atendimento")
        print(linha())
        chatGPT.text_to_speech("Espere até o final para falar! Faça uma pergunta para o Atendente ou Fale 'sair' para finalizar o atendimento\n")
        pergunta = chatGPT.speech_to_text()
        if pergunta == "sair":
            print("Finalizando atendimento ...")
            chatGPT.text_to_speech("Finalizando atendimento")
            break
        resp = chatGPT.obter_resposta(pergunta)
        print(f"Resposta: {resp} \nResposta em áudio:")
        chatGPT.text_to_speech(resp)
        print(linha())

def conheca_nossas_solucoes():
    cabeçalho('Conheça nossas soluções')
    while True:
        chatGPT.text_to_speech("Escolha 1 opção.")
        menu(["Soluções Recursos Humanos", "Soluções Marketing", "Soluções Financeiro", "Soluções Atendimento ao cliente", "Soluções T.I", "Sair do menu de soluções"])
        menu1 = ["1 para, Soluções Recursos Humanos", "2 para, Soluções Marketing", "3 para, Soluções Financeiro", "4 para, Soluções Atendimento ao cliente", "5 para, Soluções T.I", "6 para, Sair do menu de soluções"]
        opc_1 = [1, "um", "primeira opção", "a primeira opção", "opção um", "a primeira"]
        opc_2 = [2, "dois", "segunda opção", "a segunda opção", "opção dois", "a segunda"]
        opc_3 = [3, "três", "terceira opção", "a terceira opção", "opção três", "a terceira"]
        opc_4 = [4, "quatro", "quarta opção", "a quarta opção", "opção quatro", "a quarta"]
        opc_5 = [5, "cinco", "quinta opção", "a quinta opção", "opção cinco", "a quinta"]
        opc_6 = [6, "seis", "sexta opção", "a sexta opção", "opção seis", "a sexta"]

        c = 11
        for i in menu1:
            chatGPT.text_to_speech(i)

        resposta = chatGPT.opc_menu()
        if resposta == None:
            resposta = leiaInt('\033[32mSua opção: \033[m')
            resposta

        if resposta in opc_1:
            cabeçalho('Soluções Recursos Humanos')
            chatGPT.text_to_speech("Vamos fazer um tour pela página de Soluções Recursos Humanos")
            driver = ChromeDriver()
            driver.acessa_site(site)
            driver.navega_ate_uma_solucao(xpaths= xpaths, indice=0)
            driver.encerra_processo()

        elif resposta in opc_2:
            cabeçalho('Soluções Marketing')
            chatGPT.text_to_speech("Vamos fazer um tour pela página de Soluções Marketing")
            driver = ChromeDriver()
            driver.acessa_site(site)
            driver.navega_ate_uma_solucao(xpaths= xpaths, indice=1)
            time.sleep(3)
            driver.encerra_processo()

        elif resposta in opc_3:
            cabeçalho('Soluções Financeiro')
            chatGPT.text_to_speech("Vamos fazer um tour pela página de Soluções Financeiro")
            driver = ChromeDriver()
            driver.acessa_site(site)
            driver.navega_ate_uma_solucao(xpaths= xpaths, indice=2)
            time.sleep(3)
            driver.encerra_processo()
            
        elif resposta in opc_4:
            cabeçalho('Soluções Atendimento ao cliente')
            chatGPT.text_to_speech("Vamos fazer um tour pela página de Soluções Atendimento ao cliente")
            driver = ChromeDriver()
            driver.acessa_site(site)
            driver.navega_ate_uma_solucao(xpaths= xpaths, indice=3)
            time.sleep(3)
            driver.encerra_processo()

        elif resposta in opc_5:
            cabeçalho('Soluções T.I')
            chatGPT.text_to_speech("Vamos fazer um tour pela página de Soluções T.I")
            driver = ChromeDriver()
            driver.acessa_site(site)
            driver.navega_ate_uma_solucao(xpaths= xpaths, indice=4)
            time.sleep(3)
            driver.encerra_processo()

        elif resposta in opc_6:
            break

def fale_conosco():
    cabeçalho('Fale conosco')
    driver = ChromeDriver()
    driver.acessa_site(site)
    driver.entra_chat_duvida()
    time.sleep(10)
    driver.encerra_processo()

def quem_somos():
    driver = ChromeDriver()
    driver.acessa_site(site)
    driver.exibe_opcs_menu()

def menu_principal():
    while True:
        menu(["Pesquisar", "Pesquisar por voz", "Conheça nossas soluções", "Fale conosco", "Quem somos", "Sair do menu"])
        chatGPT.text_to_speech("Escolha 1 opção.")
        exibir_menu(["Pesquisar", "Pesquisar por voz", "Conheça nossas soluções", "Fale conosco", "Quem somos", "Sair do menu"])
        opc_1 = [1, "um", "primeira opção", "a primeira opção", "opção um", "a primeira"]
        opc_2 = [2, "dois", "segunda opção", "a segunda opção", "opção dois", "a segunda"]
        opc_3 = [3, "três", "terceira opção", "a terceira opção", "opção três", "a terceira"]
        opc_4 = [4, "quatro", "quarta opção", "a quarta opção", "opção quatro", "a quarta"]
        opc_5 = [5, "cinco", "quinta opção", "a quinta opção", "opção cinco", "a quinta"]
        opc_6 = [6, "seis", "sexta opção", "a sexta opção", "opção seis", "a sexta"]

        resposta = chatGPT.opc_menu()
        
        if resposta is None:
            resposta = leiaInt('\033[32mSua opção: \033[m')

        if resposta in opc_1:
            atendente_plusoft()
        elif resposta in opc_2:
            atendente_por_voz()
        elif resposta in opc_3:
            conheca_nossas_solucoes()   
        elif resposta in opc_4:
            fale_conosco()
        elif resposta in opc_5:
            quem_somos()
        elif resposta in opc_6:
            cabeçalho('Saindo do sistema')
            break
        else:
            print("\033[31mERRO! Digite uma opção válida!\033[m")

api_key = 'sua_chave_api'
chatGPT = GPT(api_key=api_key)
