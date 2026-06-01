from flask import Flask, request, jsonify, render_template
from google import genai
from dotenv import load_dotenv
from memory import add_message, get_history
from sentiment import detect_sentiment
from emergency import check_emergency
import os

load_dotenv()

app = Flask(__name__)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_input = data["message"]

    sentiment = detect_sentiment(user_input)
    emergency = check_emergency(user_input)

    history = get_history()

    prompt = f"""
Conversation History:
{history}

User Sentiment:
{sentiment}

Current Message:
{user_input}

Provide a helpful and supportive response.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text

    add_message("User", user_input)
    add_message("Bot", reply)

    return jsonify({
        "reply": reply,
        "sentiment": sentiment,
        "emergency": emergency
    })

if __name__ == "__main__":
    app.run(debug=True)