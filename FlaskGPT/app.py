from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

app = Flask(__name__)

# Set your OpenAI API key as environment variable for safety
client = OpenAI()

@app.route('/')
def home():
    test_key = os.getenv("TEST_KEY")
    return render_template('index.html',data=test_key)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    response = client.chat.completions.create(
        model='gpt-5-nano',  # gpt-5-nano is the cheapest model right now
        messages=[{'role': 'user', 'content': user_message}],
        max_tokens=20,
        temperature=0.4
    )

    reply = response.choices[0].message.content.strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

