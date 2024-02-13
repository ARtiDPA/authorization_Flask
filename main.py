from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Главная станица"


@app.route("/auth")
def add_route():
    return render_template("auth.html", loginnotfound=True)


if __name__ == "__main__":
    app.run()
