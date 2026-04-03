"""
Phase 1: Rule-Based Chatbot
============================
The simplest type of chatbot. It works by checking the user's message
against a set of keywords and rules, then returning a pre-written response.

How it works:
- User sends a message
- We check if any known keywords appear in the message
- We return the matching response, or a fallback if nothing matches

Pros: Fast, predictable, no external dependencies
Cons: Can't handle anything outside its defined rules
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="../shared/templates")


# ─── The "brain" of the rule-based bot ────────────────────────────────────────
# Each rule is a tuple: (list_of_keywords, response)
# If ANY keyword in the list appears in the user's message, we use that response.
RULES = [
    # Greetings
    (["hello", "hi", "hey", "howdy", "hiya"],
     "Hello! 👋 Great to meet you. How can I help you today?"),

    # Farewells
    (["bye", "goodbye", "see you", "later", "take care"],
     "Goodbye! Have a wonderful day! 👋"),

    # How are you
    (["how are you", "how's it going", "how do you do", "you okay"],
     "I'm just a bot, but I'm doing great! Thanks for asking 😊"),

    # Name
    (["your name", "who are you", "what are you"],
     "I'm RuleBot — a simple rule-based chatbot! I respond based on keywords in your message."),

    # Help
    (["help", "what can you do", "commands", "features"],
     "I can respond to greetings, answer questions about myself, tell jokes, "
     "give the time, and chat about the weather. Try asking me something!"),

    # Jokes
    (["joke", "funny", "laugh", "humor"],
     "Why don't scientists trust atoms? Because they make up everything! 😄"),

    # Weather
    (["weather", "rain", "sunny", "forecast", "temperature"],
     "I can't check live weather, but I hope it's sunny wherever you are! ☀️"),

    # Time / date
    (["time", "date", "today", "day"],
     f"I don't have a clock, but your device does! Check the top of your screen."),

    # Thanks
    (["thank", "thanks", "appreciate", "cheers"],
     "You're welcome! Happy to help 😊"),

    # Feelings
    (["sad", "upset", "depressed", "unhappy", "lonely"],
     "I'm sorry to hear that 😔 Remember: it's okay to reach out to someone you trust."),

    (["happy", "great", "awesome", "fantastic", "excited"],
     "That's wonderful to hear! 🎉 Keep that positive energy going!"),

    # About chatbots
    (["chatbot", "ai", "artificial intelligence", "machine learning"],
     "Great topic! I'm the simplest kind of chatbot — rule-based. "
     "More advanced bots use ML models or large language models like Claude."),
]

FALLBACK = (
    "Hmm, I'm not sure how to respond to that. 🤔 "
    "I'm a simple rule-based bot, so I only understand certain keywords. "
    "Try asking about the weather, jokes, or just say hi!"
)
# ──────────────────────────────────────────────────────────────────────────────


def get_response(user_message: str) -> str:
    """
    Find the best response for a user message by scanning for keywords.
    The message is lowercased so matching is case-insensitive.
    """
    message = user_message.lower()

    for keywords, response in RULES:
        if any(keyword in message for keyword in keywords):
            return response

    return FALLBACK


@app.route("/")
def index():
    return render_template(
        "chat.html",
        title="Rule-Based Chatbot",
        subtitle="Phase 1 — Keyword matching",
        badge="Rule-Based",
        greeting="Hi! I'm RuleBot 🤖 I respond based on keywords. Try saying 'hello', 'tell me a joke', or 'how are you'!",
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please say something!"})

    response = get_response(user_message)
    return jsonify({"response": response})


if __name__ == "__main__":
    print("Starting Rule-Based Chatbot on http://localhost:5000")
    app.run(debug=True)
