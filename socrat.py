from groq import Groq
import os 

os.environ["GROQ_API_KEY"] = "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"

client = Groq()

system_message = {
    "role":"system",
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

while True:
    user_input= input("You: ")
    
    # exit if user type exit 
    if user_input.lower() == "exit":
        break
    
    user_message = {
        "role":"user",
        "content": user_input
    }
    
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[system_message, user_message],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    print("AI :", end="")

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
    print() # for new line