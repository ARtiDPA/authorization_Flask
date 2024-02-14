from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Главная станица"


@app.route("/auth")
def auth():
    return render_template("auth.html", loginnotfound=True)


@app.route("/register")
def regit_roupe():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
