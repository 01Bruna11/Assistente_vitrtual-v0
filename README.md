# Assistente Virtual Smoak

Assistente virtual em Python capaz de:
- Reconhecer voz (SpeechRecognition)
- Falar respostas (gTTS / pyttsx3)
- Abrir sites (Google, YouTube, WhatsApp Web)
- Abrir programas (Blender, Notepad)
- Digitar textos usando pyautogui
- Controlar o Windows (shutdown)
- Futuro: adicionar interface estilo Jarvis

## Como rodar

```bash
pip install -r requirements.txt
python assistente.py

## Exemplo de estrutura de comandos já disponíveis

```bash
commands = {
    "ola": "Olá! Como posso ajudar?",
    "ajuda": "Lista de comandos disponíveis: ola, ajuda, horario, sobre",
    "horario": "O horário atual será exibido aqui futuramente.",
    "sobre": "Este é um assistente simples criado para testes."
}
