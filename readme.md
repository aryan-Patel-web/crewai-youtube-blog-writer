# CrewAI YouTube Blog Writer

🚀 This project automates researching YouTube video content and generating blog posts using [CrewAI](https://docs.crewai.com), Groq’s LLMs, and LangChain tools.

It:

✅ Searches videos on a YouTube channel  
✅ Extracts video transcriptions and insights  
✅ Generates structured blog posts  
✅ Runs multi-agent workflows in sequence

---

## 🔧 Tech Stack

- [CrewAI](https://docs.crewai.com) – multi-agent orchestration
- Groq LLMs via LangChain
- YoutubeSearchTool (CrewAI tools)
- Python

---

## 💡 How it Works

1. **Blog Researcher Agent**
   - Finds relevant YouTube videos about a given topic
   - Extracts transcription and insights

2. **Blog Writer Agent**
   - Summarizes the insights into a structured blog post

3. **Tasks**
   - Research task → pulls video data
   - Writing task → generates blog article

Agents and tasks are orchestrated via CrewAI.

---

## ⚙️ Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/crewai-youtube-blog-writer.git
cd crewai-youtube-blog-writer

agents.py          # CrewAI agent definitions
task.py            # CrewAI task definitions
crew.py            # Orchestration script
tool.py            # YouTube tool definition
requirements.txt   # Python dependencies


pip install -r requirements.txt
crewai
crewai-tools
langchain
langchain-groq
langchain-community
python-dotenv


Set Environment Variables
Create a .env file like:


GROK_API_KEY=YOUR_GROQ_API_KEY
GROQ_MODEL_NAME=gemma-7b-it


🚀 Run the Pipeline
Run the crew from the CLI:


python crew.py

📝 Output
Generates a file:

cpp
Copy
Edit
new-blog-post.md


🙏 Acknowledgements
CrewAI
LangChain
Groq

👨‍💻 Author
Aryan Patel
