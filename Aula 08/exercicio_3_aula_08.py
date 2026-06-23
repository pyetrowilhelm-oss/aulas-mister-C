from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return "Seja bem-vindo a nossa API!"

@app.route("/data")
def data():
    return str(date.today())

if __name__ == "__main__":
    app.run(debug=True)
