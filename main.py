from flask import Flask, render_template, request, redirect, url_for, make_response
from session import register, authorization, changing_mail, changing_login, changing_password
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from authentication import create_access_token, create_refresh_token
from datetime import timedelta
import authentication

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_keyy"
app.config["JWT_SECRET_KEY"] = "secret_keyy"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
app.config["JWT_REFRESH_TOKEN_EXPRIRES"] = timedelta(days=7)
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        if login != "" and password != "":
            id = authorization(login, password)
            if id:
                access_token = create_access_token(id)
                refresh_token = create_refresh_token(id)
                response = make_response(redirect(url_for("profile")))
                response.set_cookie('access_token_cookie', access_token)
                response.set_cookie('refresh_token_cookie', refresh_token)
                print(access_token)
                print(refresh_token)
                return response
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
@jwt_required(locations=["headers", "cookies"])
def profile():
    return render_template("profil.html")


@app.route("/changing_login", methods=["POST", "GET"])
@jwt_required(locations=["headers", "cookies"])
def changing_login_user():
    if request.method == "POST":
        login = request.form["login"]
        id = authentication.get_jwt_identity()
        print(id)
        changing_login(login, id)
        return "Логин успешно изменён"
    else:
        return render_template("Changing_login.html")


@app.route("/changing_mail", methods=["POST", "GET"])
@jwt_required(locations=["headers", "cookies"])
def changing_mail_user():
    if request.method == "POST":
        mail = request.form["mail"]
        id = authentication.get_jwt_identity()
        changing_mail(mail, id)
        return "mail успешно изменён"
    else:
        return render_template("Changing_mail.html")


@app.route("/changing_password", methods=["POST", "GET"])
@jwt_required(locations=["headers", "cookies"])
def changing_password_user():
    if request.method == "POST":
        password = request.form["password"]
        id = authentication.get_jwt_identity()
        changing_password(password, id)
        return "Пароль успешно изменён"
    else:
        return render_template("Changing_password.html")


@app.route("/exit")
def exit():
    response = make_response(redirect(url_for("auth")))
    response.set_cookie("access_token_cookie", "")
    response.set_cookie("refresh_token_cookie", "")
    return response


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return redirect(url_for("access_refresh"))


@app.route("/refresh")
@jwt_required(refresh=True, locations=["headers", "cookies"])
def access_refresh():
    user_id = authentication.get_jwt_identity()
    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)
    response = make_response("Токены обновленны")
    response.set_cookie('access_token_cookie', access_token)
    response.set_cookie('refresh_token_cookie', refresh_token)
    return response


if __name__ == "__main__":
    app.run()
