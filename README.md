# 🕊️ NayePankh AI Assistant

An AI-powered web application built for **NayePankh Foundation** — an NGO empowering underprivileged youth across India through education, internships, and skill development.

This project was built as part of the **NayePankh Foundation Technical Internship Selection Task** for the roles of **Artificial Intelligence**, **AI Agent Development**, and **Vibe Coder**.

---

## 🌐 Live Demo

👉 [Click here to open the app](https://your-app.streamlit.app) *(replace with your deployed link)*

---

## ✨ Features

### 🤖 Volunteer Chatbot (AI Agent)
- Multi-turn conversational AI agent
- Answers questions about NayePankh internships, volunteer programs, certificates, and more
- Maintains chat history throughout the session
- Built with LLaMA 3.1 via Groq API

### ✍️ Campaign Content Generator (AI)
- Generates ready-to-post social media content for NayePankh campaigns
- Supports: Instagram, Twitter/X, LinkedIn, WhatsApp, Email, and Slogans
- Multiple tone options: Inspiring, Informative, Urgent, Warm, Professional
- Toggle hashtags and emojis on/off
- Download generated content as `.txt`

### ❓ FAQ Assistant
- Instant answers to common questions about NayePankh Foundation
- Quick-select preset questions or type your own
- Powered by AI with NGO-specific knowledge

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Groq API](https://console.groq.com) | LLM inference (LLaMA 3.1 8B Instant) |
| [Python](https://python.org) | Backend logic |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/nayepankh-ai-assistant.git
cd nayepankh-ai-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free Groq API key at [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
streamlit run nayepankh_ai_assistant.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
nayepankh-ai-assistant/
├── nayepankh_ai_assistant.py   # Main Streamlit application
├── requirements.txt             # Python dependencies
├── .env                         # API key (not committed to GitHub)
├── .gitignore                   # Ignores .env and cache files
└── README.md                    # Project documentation
```

---

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

> ⚠️ Never commit your `.env` file to GitHub. It is already blocked by `.gitignore`.

---

## ☁️ Deploying on Streamlit Cloud

1. Push this repo to GitHub (without `.env`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Go to **App Settings → Secrets** and add:
```
GROQ_API_KEY = "your_groq_api_key_here"
```
5. Click **Deploy** — your app will be live in minutes!

---

## 💡 How This Helps NayePankh Foundation

- **Saves time** on content creation for social media campaigns
- **Provides 24/7 support** to volunteers and applicants via AI chatbot
- **Scales communication** without adding manual workload
- **Improves accessibility** by answering FAQs instantly

---

## 👩‍💻 About the Developer

**Kavya Kamatham**
B.Tech in Computer Science (AI & ML Specialization)

- 📧 kavyakamatham147@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/your-profile)
- 🐙 [GitHub](https://github.com/your-username)

---

## 📄 License

This project was built for educational and internship selection purposes for NayePankh Foundation.