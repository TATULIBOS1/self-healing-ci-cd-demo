from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Force critical failure
    raise Exception("Critical demo failure")
    return "AI-Powered CI/CD Self-Healing Demo!"

if __name__ == '__main__':
    app.run()
