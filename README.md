#  Flask AI Agent Dashboard

A **lightweight Flask-based AI Agent Dashboard** built for GitHub Codespaces.  
This tool lets you run prebuilt AI workflows like cover letter generation, regulatory research, and job description drafting—all in-browser using the OpenAI API (or local LLMs later).

---

##  Highlights

-  **No installation needed** — just open in GitHub Codespaces  
-  **OpenAI-ready** — configure via `.env` with API keys  
-  **Modular & Extendable** — drop in new agents in `agents/` folder  
-  **Safe & Clean** — runs in isolated Codespace environment

---

##  Current Features

- Cover Letter Generator  
- Regulatory Research Tool  
- Job Description Creator  

---

##  Tech Stack

- **Flask** — simple, lightweight web framework  
- **HTML/CSS (Jinja)** — UI rendering  
- Environment-based configuration via `.env`  
- Structured routes in `routes.py` for easy extension

---

##  Quick Start (Codespaces)

1. Open in GitHub: Click **Code → Codespaces → New codespace on main**  
2. Configure `.env` (rename from `.env.example`):
   ```env
   OPENAI_API_KEY=your_api_key_here

Start the app:
python app.py

Visit http://localhost:5000 in Codespaces browser preview to interact.

Add New AI Agents
Create a new Python script in agents/, e.g.:

def run(user_input):
    # Insert prompt logic for ChatGPT or local LLM
    return generate_response(user_input)

Import your agent in routes.py and expose a new endpoint or UI button.

Project Structure

agents/            # Place your agent modules here
chat_logs/         # (Optional) store session logs
knowledge/         # (Optional) prebuilt context files or docs
templates/         # Jinja HTML files
static/            # CSS, JS, and assets
.env.example       # Example environment variables
app.py             # Flask application entrypoint
routes.py          # HTTP route definitions
requirements.txt   # Python packages
README.md          # Project overview
LICENSE           # MIT License

Why It Matters
This tool demonstrates your ability to craft usable AI tools quickly in dev environments. It’s perfect for prototyping and demos—plus it’s ready to integrate with your other AI agent systems like AnythingLLM and VagalFit.

Next Steps (Optional)
Add OAuth or auth support for secure agent access

Integrate with your web portfolio (jesseboudreau.com) as live demos

Add agent configuration UI for prompt tuning

Switch to local LLM support for offline dev and entrepreneurship demos


---
