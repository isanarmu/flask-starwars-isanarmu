from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="user")

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    climate: Mapped[str] = mapped_column(String(100), nullable=False)
    terrain: Mapped[str] = mapped_column(String(100), nullable=False)
    population: Mapped[str] = mapped_column(String(100), nullable=False)

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="planet")

class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(100), nullable=False)
    mass: Mapped[str] = mapped_column(String(20), nullable=False)

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="people")

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    userid: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planetid: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=False)    
    peopleid: Mapped[int] = mapped_column(ForeignKey('people.id'), nullable=False)    

    planet:Mapped["Planet"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")

# en algunas cosas pongo str porque a veces puede ser "unknown"    
    def serialize(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "planetid": self.planetid,
            "peopleid": self.peopleid,
        }
