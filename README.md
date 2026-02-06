# 🧠 Multi-Agent Research Assistant 🤖

A Python-based multi-agent system that uses **LLM-powered agents** (Researcher, Analyst, Writer) to collaboratively research a topic and generate a structured, high-quality report.  
The system runs fully on **local LLMs using Ollama**, enabling private and cost-free inference.

---

## 🚀 Features

- Multiple collaborating AI agents  
- Graph-based execution flow using LangGraph  
- Local LLM support via Ollama  
- Modular and extensible architecture  
- CLI-based topic input  
- Automatic report generation  

---

## 🏗 Architecture
User Topic
↓
Researcher Agent → Analyst Agent → Writer Agent
↓
Final Structured Report


**Agent Roles**

- **Researcher** → Collects relevant information  
- **Analyst** → Organizes and analyzes findings  
- **Writer** → Produces final report  

---

## 🧰 Tech Stack

- Python  
- LangChain  
- LangGraph  
- Ollama  
- TinyLlama / Phi-3  

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AnkithBinagekar/multi-agent-research-assistant.git
cd multi-agent-research-assistant
2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Install & Start Ollama

Download from: https://ollama.com

Start server:

ollama serve


Pull model:

ollama pull tinyllama

▶️ Running the Project
python graph.py


Enter a topic when prompted.

📄 Output

The final report is:

Printed in terminal

Saved as:

output.txt

🧪 Example Output
FINAL REPORT:
The Impact of Artificial Intelligence on Society

1. Ethical Considerations
2. Human-AI Collaboration
3. Economic Implications
4. Technological Advancements
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

🔮 Future Enhancements

Web search integration

Long-term memory for agents

PDF / DOCX export

Web UI

👨‍💻 Author

Ankith Binagekar
GitHub: https://github.com/AnkithBinagekar
