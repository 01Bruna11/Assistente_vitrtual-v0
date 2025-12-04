# Assistente Virtual Smoak

Assistente virtual desenvolvido em Python para testes e estudos de automação com voz, interação com o sistema e execução de tarefas no Windows.

---

## Funcionalidades

- Reconhecimento de voz com SpeechRecognition  
- Respostas por voz usando gTTS ou pyttsx3  
- Abertura de sites (Google, YouTube, WhatsApp Web)  
- Abertura de programas instalados (Blender, Notepad, etc.)  
- Digitação automática com pyautogui  
- Comandos de sistema (como desligar o computador)  
- Comandos internos simples para testes  
- Base preparada para futura interface gráfica estilo Jarvis

---

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/01Bruna11/Assistente_vitrtual-v0.git
cd Assistente_vitrtual-v0
```

### 2. Atualizar o pip (recomendado)

```bash
python -m pip install --upgrade pip
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o assistente

```bash
python assistente.py
```

---

## Comandos internos disponíveis

```python
commands = {
    "ola": "Olá! Como posso ajudar?",
    "ajuda": "Lista de comandos disponíveis: ola, ajuda, horario, sobre",
    "horario": "O horário atual será exibido aqui futuramente.",
    "sobre": "Este é um assistente simples criado para testes."
}
```

---

## Estrutura do projeto

```
Assistente_vitrtual-v0/
│── assistente.py
│── requirements.txt
│── README.md
└── outros arquivos
```

---

## Requisitos

- Python 3.9 ou superior  
- Sistema Windows  
- Microfone para reconhecimento de voz  

---

## Melhorias futuras

- Interface gráfica  
- Respostas mais inteligentes  
- Suporte offline  
- Plugins adicionais  
- Painel de configurações
