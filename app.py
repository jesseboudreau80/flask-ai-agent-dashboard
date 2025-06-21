from flask import Flask, render_template, request, jsonify
from config import Config
from agents.cover_letter import generate_cover_letter
from agents.research import run_research

from openai import OpenAI
import os
import json
from pathlib import Path
from datetime import datetime

# ✅ Modern SDK client (v1+)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Global memory: { session_id: { agent_id: [messages] } }
chat_sessions = {}

# Save directory
SAVE_DIR = Path("chat_logs")
SAVE_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-cover-letter', methods=['POST'])
def cover_letter():
    data = request.json
    center_name = data.get('center_name')
    license_type = data.get('license_type')
    result = generate_cover_letter(center_name, license_type)
    return jsonify({"output": result})


@app.route('/run-research', methods=['POST'])
def research():
    data = request.json
    location = data.get('location')
    center_type = data.get('center_type')
    center_code = data.get('center_code')
    center_name = data.get('center_name')
    services = data.get('services', {})

    result = run_research(
        location=location,
        center_type=center_type,
        services=services,
        center_code=center_code,
        center_name=center_name
    )

    return jsonify({"output": result})


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    agent_id = data.get('agent_id', 'chatbox')
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({"response": "Message cannot be empty."}), 400

    # Setup chat memory
    if session_id not in chat_sessions:
        chat_sessions[session_id] = {}
    if agent_id not in chat_sessions[session_id]:
        chat_sessions[session_id][agent_id] = []

    chat_sessions[session_id][agent_id].append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_sessions[session_id][agent_id],
            temperature=0.7
        )
        bot_reply = response.choices[0].message.content.strip()
        chat_sessions[session_id][agent_id].append({"role": "assistant", "content": bot_reply})

        print(f"[{session_id}][{agent_id}] Chat updated: {len(chat_sessions[session_id][agent_id])} messages")
        return jsonify({"response": bot_reply})
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({"response": f"⚠️ Error calling OpenAI:\n\n{str(e)}"}), 500


@app.route('/save-chat', methods=['POST'])
def save_chat():
    data = request.get_json()
    session_id = data.get('session_id')
    agent_id = data.get('agent_id')

    if not session_id or not agent_id:
        return jsonify({"status": "error", "message": "Missing session_id or agent_id"}), 400

    session = chat_sessions.get(session_id, {}).get(agent_id)
    if not session:
        return jsonify({"status": "error", "message": "No chat history found"}), 404

    timestamp = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
    filename = f"{session_id}__{agent_id}__{timestamp}.json"
    filepath = SAVE_DIR / filename

    with open(filepath, 'w') as f:
        json.dump(session, f, indent=2)

    return jsonify({"status": "success", "filename": filename})


@app.route('/chat-history', methods=['GET'])
def list_chat_logs():
    files = [f.name for f in SAVE_DIR.glob("*.json")]
    return jsonify({"files": files})


@app.route('/load-chat', methods=['POST'])
def load_chat():
    data = request.get_json()
    filename = data.get('filename')
    if not filename:
        return jsonify({"error": "No filename provided"}), 400

    filepath = SAVE_DIR / filename
    if not filepath.exists():
        return jsonify({"error": "File not found"}), 404

    with open(filepath, 'r') as f:
        history = json.load(f)

    try:
        session_id, agent_id, _ = filename.split("__")
    except:
        return jsonify({"error": "Filename format invalid"}), 400

    if session_id not in chat_sessions:
        chat_sessions[session_id] = {}
    chat_sessions[session_id][agent_id] = history

    return jsonify({"status": "success", "session_id": session_id, "agent_id": agent_id})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
