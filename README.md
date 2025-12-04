🚀 Assistente Virtual Smoak

Um assistente virtual em Python capaz de entender comandos de voz e executar ações no seu computador.
Com ele você pode abrir programas, buscar no Google, acessar sites, escrever textos e até desligar o PC usando somente sua voz.

🧠 Funcionalidades
🎤 Reconhecimento de voz

Usa SpeechRecognition com API do Google.

🔊 Síntese de voz (fala)

Usa gTTS (voz humana, natural)

Toca o áudio com playsound

🌐 Ações na internet

Pesquisa no Google

Pesquisa no YouTube

Abre WhatsApp Web

Abre URLs personalizadas (ex: Gather)

💻 Automação no Windows

Abre programas (Notepad, Blender)

Digita textos automaticamente

Move o mouse / clica (pyautogui)

Pode desligar o computador

📝 Interação com Notepad

Abre o bloco de notas

Pergunta o que você quer escrever

Digita o texto reconhecido por voz

Salva e fecha automaticamente

⌨ Teclado virtual

Abre o teclado virtual do Windows (osk)

Digita comandos por voz

🔮 Futuro (planejado)

Interface gráfica estilo Jarvis

Mais comandos

Controle por hotword permanente

Integração com APIs externas

📁 Estrutura do Projeto
assistente.py
requirements.txt
README.md

▶️ Como rodar

Instale as dependências:

pip install -r requirements.txt


Execute o assistente:

python assistente.py

🧩 Exemplo de comandos internos (texto)

Apesar de funcionar por voz, o assistente internamente possui um dicionário base (exemplo):

commands = {
    "ola": "Olá! Como posso ajudar?",
    "ajuda": "Lista de comandos disponíveis: ola, ajuda, horario, sobre",
    "horario": "O horário atual será exibido aqui futuramente.",
    "sobre": "Este é um assistente simples criado para testes."
}

🎙 Exemplos de comandos por voz
Comando falado	Ação executada
“Hey Smoak”	Saudação
“Looking for Python tutorials”	Pesquisa no Google
“Looking YouTube for Blender models”	YouTube
“Open WhatsApp”	Abre WhatsApp Web
“Open notepad”	Abre bloco de notas e digita por voz
“Power off”	Desliga o PC
“Open Blender”	Abre Blender
“Open keyboard”	Abre teclado virtual
🛠 Tecnologias utilizadas

Python 3

SpeechRecognition

PyAudio (dependência do microfone)

gTTS

playsound

pyautogui

webbrowser

tkinter (em breve interface)

📦 requirements.txt

Certifique-se de incluir:

SpeechRecognition
gTTS
playsound==1.2.2
pyautogui
pyaudio


E todas as outras libs necessárias.