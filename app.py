import openai

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
openai.api_key = "enter your api key"

conversation = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("send")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content":str(user_input)}],
            temperature=0.6,
        )
        conversation.append((user_input, response['choices'][0]['message']['content']))
        
        return redirect(url_for("index"))
    if len(conversation) == 0:
        return render_template("intro.html")
    return render_template("index.html", conversation=conversation)

