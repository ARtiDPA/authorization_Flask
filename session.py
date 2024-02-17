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
            return True
        else:
            return False
