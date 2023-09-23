import openai

from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)
openai.api_key = "ENTER YOUR API-KEY"

conversation = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("send")
        print(request.form)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[
                        {"role":"system", "content":"You are sarcastic"},
                        {"role":"user", "content":"How are you?"},
                        {"role":"assistant", "content":"I am planning on taking over the world"},
                        {"role":"user", "content":str(user_input)}
                     ], 
            temperature=0.6,
        )
        print(response.choices[0].message.content)
        return jsonify([user_input,response.choices[0].message.content])
         
    return render_template("index.html", conversation=conversation)








