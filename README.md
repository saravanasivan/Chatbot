# Groq Chatbot using LangChain and Tkinter

This project implements an AI-powered chatbot built with **LangChain** and **Groq API**.  
The chatbot features a graphical interface using **Tkinter**, maintains conversation memory, and logs each process step in the terminal for better traceability and debugging.

---

## Features

- Graphical user interface (GUI) built with Tkinter  
- Fast and efficient responses powered by Groq LLMs  
- Conversation memory for contextual responses  
- Multithreaded design to ensure smooth user experience  
- Step-by-step logs displayed in the terminal  
- Modular architecture built on LangChain

---

## Technology Stack

| Component | Description |
|------------|-------------|
| **Programming Language** | Python 3.11+ |
| **Framework** | LangChain |
| **Model Provider** | Groq Cloud API |
| **GUI Framework** | Tkinter |
| **Memory Management** | LangChain `ConversationBufferMemory` |

---

## Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/saravanasivan/groq-chatbot.git
cd groq-chatbot

---

### Step 2: Install Dependencies

pip install langchain groq langchain-groq python-dotenv

---

### Step 3: Add Your Groq API Key

You can obtain your API key from the ==>> https://console.groq.com/keys

---

Step 4: Run the Chatbot

python Groq_Chatbot_GUI.py
