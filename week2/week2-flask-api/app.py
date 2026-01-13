from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.get("/time")
def get_time():
    return jsonify({"time": time.strftime("%H:%M:%S")})

@app.get("/joke")
def get_joke():
    jokes = ["Why did the cat join a band?Because it wanted to be a purr-cussionist!",
             "What do you call a fake noodle? An impasta!",
             "Why did the scarecrow win an award? Because he was outstanding in the field!",
             "Why did the coffee file a police report? It got mugged!",
             "Why do programmers hate nature? Too many bugs"]
    return jsonify({"joke": random.choice(jokes)})

@app.post("/echo")
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(debug=True)