from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
import database


class user(database.Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    mail: Mapped[str] = mapped_column(String, nullable=False)
    login: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)


def create_tables():
    database.Base.metadata.create_all(database.engine)
