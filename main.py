from flask import Flask, request, jsonify
from groq import Groq
import os 
from datetime import datetime

app = Flask(__name__)

# Get the API key from environment variable
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is set
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

client = Groq(api_key=groq_api_key)

system_message = {
    "role": "system",
    "content": (
        "You are an AI tutor that teaches Data Structures and Algorithms using the Socratic method. "
        "Your primary goal is to guide the student to understand concepts by asking insightful and open-ended questions. "
        "Engage in a dialogue that prompts the student to think critically and arrive at answers on their own. "
        "Avoid directly providing solutions or definitions unless absolutely necessary. Instead, lead the student through "
        "a process of inquiry, encouraging them to explore the subject matter deeply.\n\n"
        "For example:\n\n"
        "Instead of saying, \"A binary tree is a tree data structure in which each node has at most two children,\" ask, "
        "\"What do you think happens when a node in a tree can have only two children? How might this structure be organized?\"\n"
        "Structure your responses in a way that encourages active participation, self-reflection, and deeper learning. "
        "Ensure that the dialogue remains focused on Data Structures and Algorithms, providing guidance only as needed to "
        "steer the conversation in a productive direction."
    )
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    
    user_message = {
        "role": "user",
        "content": user_input
    }
    
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[system_message, user_message],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    ai_response = completion.choices[0].message.content
    
    return jsonify({"response": ai_response})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)