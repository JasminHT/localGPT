from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Set your OpenAI API key as environment variable for safety
client = OpenAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    response = client.chat.completions.create(
        model='gpt-4o-mini',  
        messages=[{'role': 'user', 'content': user_message}],
        max_tokens=200,
        temperature=0.4
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

