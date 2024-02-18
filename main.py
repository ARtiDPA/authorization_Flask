from flask import Flask, render_template, request, redirect, url_for
from session import register, authorization, serching_user
from authentication import create_token, check
import flask

app = Flask(__name__)
app.secret_key = ["qazwsxedc_QAZWSXEDC"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        print(login)
        print(password)
        if login != "" and password != "":
            id = authorization(login, password)
            if id:
                token = create_token(id)
                flask.session["user_id"] = token
                return redirect(url_for("profile"))
            else:
                return render_template("auth.html", valid_data=True)
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
                return redirect(url_for("auth"))
            else:
                return "пароли должны совпадать"
        else:
            return "Поля не могут быть пустыми"
    else:
        return render_template("register.html")


@app.route("/profile", methods=["GET"])
def profile():
    if "user_id" in flask.session:
        user_token = flask.session["user_id"]
        print("prov_1")
        if user_token != "":
            print("prove_2")
            id = check(user_token)
            if serching_user(id):
                print("prove_3")
                return render_template("profil.html")
            else:
                return redirect(url_for("auth"))
        else:
            return redirect(url_for("auth"))
    else:
        return redirect(url_for("auth"))


@app.route("/exit")
def exit():
    if "user_id" in flask.session:
        user_token = flask.session["user_id"]
        if user_token != "":
            flask.session["user_id"] = ""
            return redirect(url_for("auth"))
    else:
        return redirect(url_for("auth"))


if __name__ == "__main__":
    app.run()
