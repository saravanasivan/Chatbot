import os
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# ----------------------------------------
# STEP 1: Load API key and initialize model
# ----------------------------------------
print("[INFO] Loading environment variables...")
load_dotenv()

print("[INFO] Initializing Groq LLM...")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # ✅ currently active Groq model
    temperature=0.7,
)

# ----------------------------------------
# STEP 2: Setup memory (for conversation context)
# ----------------------------------------
print("[INFO] Initializing memory...")
memory = ConversationBufferMemory(return_messages=True)

print("[INFO] Creating conversation chain...")
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# ----------------------------------------
# STEP 3: Tkinter GUI Setup
# ----------------------------------------
root = tk.Tk()
root.title("Groq Chatbot 🧠")
root.geometry("700x600")
root.resizable(False, False)

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_display.config(state=tk.DISABLED)

user_input = tk.Entry(root, font=("Consolas", 12))
user_input.pack(padx=10, pady=5, fill=tk.X)

# ----------------------------------------
# STEP 4: Function to handle chat interaction
# ----------------------------------------
def send_message():
    user_text = user_input.get().strip()
    if not user_text:
        return

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_text}\n", "user")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)
    user_input.delete(0, tk.END)

    # Run the model response in a separate thread
    threading.Thread(target=generate_response, args=(user_text,)).start()

def generate_response(user_text):
    print(f"[STEP] User asked: {user_text}")
    print("[INFO] Sending to Groq model...")

    try:
        response = conversation.invoke({"input": user_text})
        reply = response["response"]
        print("[SUCCESS] Model replied successfully!")

    except Exception as e:
        reply = f"[Error] {e}"
        print("[ERROR]", e)

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Bot: {reply}\n\n", "bot")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

# ----------------------------------------
# STEP 5: Bind Enter key and send button
# ----------------------------------------
user_input.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", font=("Consolas", 12), command=send_message)
send_button.pack(pady=5)

# ----------------------------------------
# STEP 6: Run GUI Loop
# ----------------------------------------
print("[READY] Groq Chatbot GUI started successfully!")
print("[HINT] Type inside the window, or press Enter to send message.")
print("[MEMORY] All conversation context is stored in memory for future responses.\n")

root.mainloop()
