from flask import Flask, render_template, request, jsonify
from config import Config
from agents.cover_letter import generate_cover_letter
from agents.research import run_research

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
    result = run_research(location)
    return jsonify({"output": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
