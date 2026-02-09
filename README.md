# 🧠 Multi-Agent Research Assistant (Local LLMs)

A **multi-agent AI system** built in Python where specialized agents collaborate to **simulate a research workflow** and generate a structured report from a user-provided topic.

The project focuses on **agent orchestration, reasoning flow, and system design**, running entirely on **local LLMs via Ollama** — no paid APIs, no cloud dependency.

---

## 🚀 Key Highlights

- Multi-agent architecture with clear role separation  
- Sequential research → analysis → writing workflow  
- Fully local, cost-free LLM inference using Ollama  
- Modular and extensible agent/task design  
- CLI + backend integration ready for UI consumption  
- Designed to demonstrate **agent reasoning**, not just text generation  

---

## 🧠 What This Project Demonstrates

This project is intended to showcase:

- **Agent collaboration patterns**
- **LLM-driven reasoning workflows**
- **Task decomposition and execution**
- **End-to-end AI system integration**

> ⚠️ **Important Note**  
> This system currently runs **without live web search or retrieval**.  
> All outputs are generated based on the LLM’s internal knowledge and **may not be factually accurate**.  
> This is a **known and intentional limitation**, addressed in the Future Enhancements section.

---

## 🏗️ System Architecture
# 🧠 Multi-Agent Research Assistant (Local LLMs)

A **multi-agent AI system** built in Python where specialized agents collaborate to **simulate a research workflow** and generate a structured report from a user-provided topic.

The project focuses on **agent orchestration, reasoning flow, and system design**, running entirely on **local LLMs via Ollama** — no paid APIs, no cloud dependency.

---

## 🚀 Key Highlights

- Multi-agent architecture with clear role separation  
- Sequential research → analysis → writing workflow  
- Fully local, cost-free LLM inference using Ollama  
- Modular and extensible agent/task design  
- CLI + backend integration ready for UI consumption  
- Designed to demonstrate **agent reasoning**, not just text generation  

---

## 🧠 What This Project Demonstrates

This project is intended to showcase:

- **Agent collaboration patterns**
- **LLM-driven reasoning workflows**
- **Task decomposition and execution**
- **End-to-end AI system integration**

> ⚠️ **Important Note**  
> This system currently runs **without live web search or retrieval**.  
> All outputs are generated based on the LLM’s internal knowledge and **may not be factually accurate**.  
> This is a **known and intentional limitation**, addressed in the Future Enhancements section.

---

## 🏗️ System Architecture
User Topic
↓
Researcher Agent
↓
Analyst Agent
↓
Writer Agent
↓
Final Structured Report


### 🧑‍🤝‍🧑 Agent Roles

- **Researcher**  
  Simulates information gathering and topic exploration.

- **Analyst**  
  Extracts insights, identifies themes, and organizes findings.

- **Writer**  
  Produces a coherent, structured final report.

---

## 🧰 Tech Stack

- Python  
- CrewAI  
- LangChain  
- LangGraph  
- Ollama (Local LLM Runtime)  
- TinyLlama / Phi-3 / Llama 3  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnkithBinagekar/multi-agent-research-assistant.git
cd multi-agent-research-assistant
2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Start Ollama

Download Ollama:
https://ollama.com

Start the server:

ollama serve


Pull a lightweight model (recommended for 8GB RAM):

ollama pull tinyllama

▶️ Running the Project
python graph.py


Enter a topic when prompted (e.g., Goa Tourism, Future of AI).

📄 Output

Final report is printed in the terminal

Optionally saved to output.txt

🧪 Sample Output (Excerpt)

FINAL REPORT: Future of Artificial Intelligence

1. Overview of AI Evolution
2. Applications Across Industries
3. Ethical & Societal Implications
4. Limitations and Challenges
5. Future Outlook

📁 Project Structure
multi-agent-research-assistant/
│
├── agents.py
├── tasks.py
├── graph.py
├── llm.py
├── config.py
├── requirements.txt
├── README.md
└── output.txt


Future Enhancements

🌐 Web search integration (DuckDuckGo / Wikipedia)

📚 Retrieval-Augmented Generation (RAG)

🧠 Long-term agent memory

📄 PDF / DOCX export

🖥️ Full web-based UI

✅ Fact grounding and citations

👨‍💻 Author

Ankith Binagekar
GitHub: https://github.com/AnkithBinagekar
