from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "FX Master is running!"

if __name__ == "__main__":
    app.run()
    
