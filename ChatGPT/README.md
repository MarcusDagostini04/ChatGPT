# Projeto ChatGPT - Hear Me Out - Plusoft

## Autocrítica

Iniciamos desanimados devido à saída de membros da equipe, levando à fusão com outro grupo. Embora tenha proporcionado compartilhamento de experiências, a limitação de seis membros nos impediu de participar do NEXT, resultando na persistência da ideia inicial, sem muitas expectativas.

No início, o processo mais complicado envolveu a configuração do ChatGPT, a criação de uma classe para abstrair o chat, e a configuração das bibliotecas pyttsx3 e Speech_recognition para transformação de texto em áudio e vice-versa. Posteriormente, desenvolvemos uma automação web usando Selenium para apresentar as soluções da Plusoft. Inicialmente, enfrentamos problemas ao tentar gravar a tela para apresentação, resultando na escolha do PyAutoGUI. Foram necessários "time.sleep()" para evitar erros durante a execução. Na última entrega, encontramos uma configuração para o webdriver que permite a execução em segundo plano, permitindo gravar a tela, melhorando a experiência do usuário.

Aprendemos a lidar com tratamento de exceções, evitando possíveis erros do usuário e requisições, embora seja necessário aprimorar a abordagem para lidar com falhas humanas, problemas de conexão à internet ou com a api_key.

Percebemos que há muitas possibilidades de explorar na API do ChatGPT, como diversos modelos de chat, reconhecimento de imagens e de voz. Optamos por outras bibliotecas para essas funcionalidades neste projeto, já que cada opção avançada da API tem um custo associado.

## Planos de Melhoria

- Treinar o modelo para responder a questões específicas dos clientes, personalizando o atendimento.
- Melhorar a interface do menu, considerando a integração de HTML com a página do cliente para uma apresentação eficiente e atrativa.
- Implementar as melhores práticas de acessibilidade em um site para garantir uma experiência inclusiva.
- Realizar testes com usuários que necessitam de auxílio na navegação para identificar oportunidades de aprimoramento.

## Introdução
Este é um projeto que envolve automação de interações em uma aplicação web usando Selenium, PyAutoGUI e integração com o modelo de linguagem GPT-3.5 para fornecer respostas automáticas.

Classe GPT
A classe GPT é responsável pela integração com a API do OpenAI e fornece métodos para obter respostas de um modelo de linguagem.


## Estrutura do Projeto

### Classes e Módulos

- **Classe GPT (`GPT`):** Responsável por interagir com o modelo GPT-3.5-turbo da OpenAI para obter respostas a partir de perguntas fornecidas.
- **Módulo Selenium (`selenium`):** Utilizado para automatizar a interação com páginas web, incluindo a abertura e navegação.
- **Módulo PyAutoGUI (`pyautogui`):** Oferece funcionalidades de automação de tarefas GUI, permitindo a simulação de ações do mouse e do teclado.
- **Biblioteca Pyttsx3 (`pyttsx3`):** Usada para converter texto em voz, fornecendo uma funcionalidade de leitura em voz alta.
- **Biblioteca SpeechRecognition (`speech_recognition`):** Utilizada para realizar a transcrição de áudio para texto, permitindo interações por voz.
- **Biblioteca Requests (`requests`):** Usada para realizar requisições HTTP, especialmente para interagir com a API da OpenAI.

### Como Usar

1. **Configuração do Ambiente:**
   - Instale as bibliotecas necessárias executando `pip install -r requirements.txt`.
   - Certifique-se de ter o ChromeDriver instalado.

2. **Configuração da Chave da API OpenAI:**
   - Substitua `'sua_chave'` na linha `api_key = 'sua_chave'` no código pelo seu token de API da OpenAI.

3. **Executando o Projeto:**
   - Execute o script `main_Chat.py` para iniciar a interface do ChatGPT.

4. **Interagindo:**
   - Siga as instruções fornecidas no console para realizar pesquisas, interações por voz, explorar soluções e mais.

### Métodos Classe GPT:
__init__(self, api_key): Inicializa a instância com a chave da API do OpenAI, o modelo a ser usado e os links para a API.

obter_resposta(self, pergunta): Envia uma pergunta para o modelo de linguagem e retorna uma resposta.

text_to_speech(self, texto): Converta texto em discurso utilizando uma biblioteca pyttsx3.

speech_to_text(self): Converta áudio capturado por um microfone em texto utilizando uma biblioteca SpeechRecognition.

opc_menu(self): Captura opções de um menu por meio de voz e retorna o texto transcrito.

### Funções Auxiliares
leiaInt(msg): Lê um número inteiro da entrada padrão.

linha(tam=42): Retorna uma linha de caracteres "-" com um comprimento especificado.

cabeçalho(txt): Imprima um cabeçalho formatado.

menu(lista): Imprima um menu formatado com base em uma lista de opções.

### Integração com Aplicação Web
acessa_site(): Abra o navegador e acesse a página da Plusoft.

entra_chat_duvida(): Interage com o chat da página da Plusoft para enviar uma pergunta.

Função navega_ate_uma_solucao(), automatizam a navegação em diferentes soluções do site da Plusoft, como RH, Financeiro ...

### Funcionalidades Adicionais

exibir_menu(opcoes): Utilize a classe GPT para converter opções de menu em áudio.

atendente_plusoft(): Interage com o atendimento da Plusoft usando a classe GPT.

atendente_por_voz(): permite perguntas por voz usando a classe GPT.

conheca_nossas_solucoes(): Apresenta opções de soluções da Plusoft com interação via voz.

fale_conosco(): Interage com a seção "Fale Conosco" da Plusoft.

quem_somos(): Apresenta o site da Plusoft e apresnete o menu.

menu_principal(): Executa o menu principal do sistema.

## Notas Finais
Este projeto demonstra uma automação de interações em uma aplicação web e integração com um modelo de linguagem, com um pouco de melhorias de acessibilidade, reconhecendo que há muito o que se explorar nesse tema. Caso haja alguma dificuldade ou problema, entre em contato com o grupo.


## Licença

Esse projeto foi desenvolvido pelo grupo Hear Me Out, do 2º TDST, com os seguintes integrantes:
- GUILHERME HENRIQUE MELO DE OLIVEIRA – RM: 95184
- GUILHERME LUCAS ARTIGIANI – RM: 94322
- LUCAS VINICIUS OLIVEIRA GALINDO – RM: 95177
- MARCUS VINICIUS DAGOSTINI – RM: 94279
- THIAGO RIBEIRO DA COSTA – RM: 92800
- VINICIUS GONÇALVES CARNEIRO – RM: 94154

