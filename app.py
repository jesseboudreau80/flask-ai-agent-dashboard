import os
import requests
from openai import OpenAI
from config import load_config

def chat_with_model(messages, config=None):
    if config is None:
        config = load_config()

    # Load model provider preference
    provider_name = config.get("defaultModelProvider", "openai")
    providers = config.get("models", {})

    # Try primary provider first
    provider = providers.get(provider_name)
    fallback_provider = "openai" if provider_name != "openai" else None
    fallback = providers.get(fallback_provider)

    # Primary call
    try:
        if provider_name == "openrouter":
            return call_openrouter(messages, provider)
        elif provider_name == "openai":
            return call_openai(messages, provider)
    except Exception as e:
        print(f"[!] Primary provider '{provider_name}' failed: {e}")

    # Fallback call
    if fallback:
        try:
            print("[*] Trying fallback provider: OpenAI")
            return call_openai(messages, fallback)
        except Exception as e:
            print(f"[!] Fallback provider also failed: {e}")

    raise Exception("All providers failed to respond.")

# ===== OpenRouter LLM Call =====
def call_openrouter(messages, provider):
    api_base = provider.get("apiBase", "https://openrouter.ai/api/v1")
    api_key = provider.get("apiKey")
    model = provider.get("defaultModel")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
    }

    response = requests.post(f"{api_base}/chat/completions", json=payload, headers=headers)
    response.raise_for_status()

    reply = response.json()["choices"][0]["message"]["content"]
    return reply.strip()

# ===== OpenAI Direct LLM Call =====
def call_openai(messages, provider):
    api_key = provider.get("apiKey") or os.getenv("OPENAI_API_KEY")
    model = provider.get("defaultModel", "gpt-3.5-turbo")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def home():
    return render_template('index.html')  # assumes you have templates/index.html

if __name__ == '__main__':
    app.run()
