from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    # 30% chance of failure
    if random.random() < 0.3:
        raise RuntimeError("Simulated error!")
    return "CI/CD Self-Healing Demo!"

if __name__ == '__main__':
    app.run()
