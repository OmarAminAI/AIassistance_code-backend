import requests

GROQ_API_KEY = "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"

def generate_code(prompt: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant who generates code based on user prompts."},
            {"role": "user", "content": f"Generate code for the following request:\n\n{prompt}"}
        ],
        "temperature": 0.4
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        return f"Groq API Error: {str(e)}"
    except Exception as e:
        return f"Internal Error: {str(e)}"
