from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone:Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    favorite_characters:Mapped[list['FavoriteCharacters']] = relationship(back_populates='user')
    favorite_planets:Mapped[list['FavoritePlanets']] = relationship(back_populates='user')
    favorite_starships:Mapped[list['FavoriteStarships']] = relationship(back_populates='user')



class Characters(db.Model):
    __tablename__='characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name_character:Mapped[str] = mapped_column(String(50), nullable=False)
    gender:Mapped[str] = mapped_column(String(50))
    height:Mapped[int] = mapped_column(Integer)
    weigth:Mapped[int] = mapped_column(Integer)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planet:Mapped['Planets'] = relationship(back_populates='id_characters')
    favorite_characters:Mapped[list['FavoriteCharacters']] = relationship(back_populates='character')

class Planets(db.Model):
    __tablename__='planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name_planet:Mapped[str] = mapped_column(String(50), nullable=False)
    climate:Mapped[str] = mapped_column(String(50))
    poblation:Mapped[int]= mapped_column(Integer)
    id_characters:Mapped[list['Characters']] = relationship(back_populates='planet')
    favorite_planets:Mapped[list['FavoritePlanets']] = relationship(back_populates='planet')

class Starships(db.Model):
    __tablename__='starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    name_starship:Mapped[str] = mapped_column(String(50), nullable=False)
    passengers:Mapped[int] = mapped_column(Integer)
    favorite_starships:Mapped[list['FavoriteStarships']] = relationship(back_populates='starships')

class FavoriteCharacters(db.Model):
    __tablename__='favorite_characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
    user:Mapped['User'] = relationship(back_populates='favorite_characters')
    character_id:Mapped[int] = mapped_column(ForeignKey('characters.id'))
    character:Mapped['Characters'] = relationship(back_populates='favorite_characters')

class FavoritePlanets(db.Model):
    __tablename__='favorite_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
    user:Mapped['User'] = relationship(back_populates='favorite_planets')
    planet_id:Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planet:Mapped['Planets'] = relationship(back_populates='favorite_planets')


class FavoriteStarships(db.Model):
    __tablename__='favorite_starships'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('user.id'))
    user:Mapped['User'] = relationship(back_populates='favorite_starships')
    starship_id:Mapped[int] = mapped_column(ForeignKey('starships.id'))
    starship:Mapped['Starships'] = relationship(back_populates='favorite_starships')