from flask import Flask, render_template, request
from session import register, authorization


app = Flask(__name__)


@app.route("/")
def index():
    return "Главная станица"


@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        print(login)
        print(password)
        if login != "" and password != "":
            if authorization(login, password):
                return "Все четко"
            else:
                return "Все плохо"
        else:
            return "Поля пустые"
    else:
        return render_template("auth.html", loginnotfound=True)


@app.route("/register", methods=["POST", "GET"])
def register_roupe():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        mail = request.form["mail"]
        login = request.form["login"]
        password_1 = request.form["password_1"]
        password_2 = request.form["password_2"]
        register_date = [name, surname, mail, login, password_1, password_2]
        if all(register_date):
            if password_1 == password_2:
                register(name, surname, mail, login, password_1)
                return render_template("auth.html")
            else:
                return "пароли должны совпадать"
        else:
            return "Поля не могут быть пустыми"
    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run()
