import pip

# Install g4f if not installed
pip.main(['install', 'g4f'])

from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route('/', methods=['POST'])
def do_chat():
    try:
        data = request.json
        user_message = data.get('message')
        if user_message:
            # Requesting chat completions from g4f client
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
            )
            # Extracting bot's response from the completion
            bot_response = response.choices[0].message.content if response.choices else "No response"
        else:
            bot_response = "Please enter a message"
    except Exception as e:
        bot_response = f"Error: {str(e)}"

    # Returning bot's response as JSON
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 6768
    print(f"Server running on {host}:{port}")
    app.run(host=host, port=port)
