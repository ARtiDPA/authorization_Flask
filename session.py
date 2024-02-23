from database import Session
from models import user
from sqlalchemy import select


def register(name, surname, mail, login, password):
    with Session.begin() as session:
        session.add(user(name=name, surname=surname, mail=mail, login=login, password=password))
        session.commit()


def authorization(login, password):
    with Session.begin() as session:
        stm = select(user).filter_by(login=login, password=password)
        user_info = session.scalars(stm).all()
        print(user_info)
        print(stm)
        if user_info != []:
            return user_info[0].id
        else:
            return False


def serching_user(id):
    with Session.begin() as session:
        stm = select(user).filter_by(id=id)
        user_info = session.scalars(stm).all()
        print(user_info[0].id)
        if user_info != []:
            return True
        else:
            return False


def changing_login(login, id):
    with Session.begin() as session:
        user_object = session.get(user, id)
        user_object.login = login
        session.commit


def changing_mail(mail, id):
    with Session.begin() as session:
        user_object = session.get(user, id)
        user_object.mail = mail
        session.commit


def changing_password(password, id):
    with Session.begin() as session:
        user_object = session.get(user, id)
        user_object.password = password
        session.commit
