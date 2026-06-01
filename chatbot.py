from google import genai
from dotenv import load_dotenv
from memory import add_message, get_history
from sentiment import detect_sentiment
from emergency import check_emergency
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Mental Health Chatbot Started")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    sentiment = detect_sentiment(user_input)

    emergency = check_emergency(user_input)

    history = get_history()

    prompt = f"""
Conversation History:
{history}

User Sentiment: {sentiment}

Current Message:
{user_input}

Respond naturally and supportively.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text

    add_message("User", user_input)
    add_message("Bot", reply)

    print("\nBot:", reply)

    print("\nSentiment:", sentiment)

    if emergency:
        print("⚠ EMERGENCY ALERT DETECTED")

    print()