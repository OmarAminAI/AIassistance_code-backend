import requests

GROQ_API_KEY = "GROQ_API_KEY"

def explain_code(code: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who explains code."},
            {"role": "user", "content": f"Explain what this code does:\n\n{code}"}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        return f"Groq API Error: {str(e)}"
    except Exception as e:
        return f"Internal Error: {str(e)}"
