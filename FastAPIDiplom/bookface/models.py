from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

"""В данном модуле определены столбцы таблиц, их типы данных и ограничения.
Отношения между моделями с использованием relationship (один-ко-многим)"""

Base = declarative_base()
"""Создание базового класса Base, 
который используется для описания моделей базы данных"""

class CustomUser(Base):
    """Класс модели CustomUser, который наследуется от базового класса Base.
    """
    __tablename__ = 'users' # Указание имени таблицы в базе данных.

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
    hashed_password = Column(String, nullable=False)


    def __repr__(self):
        return f'{self.first_name} {self.last_name}' # Строковое представление объекта CustomUser



# Фото пользователя
class Photo(Base):
    """Класс модели Photo,
    который наследуется от базового класса Base"""
    __tablename__ = 'photos' # Указание имени таблицы в базе данных.

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    filename = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user = relationship("CustomUser", back_populates="photos")

# Комментарии к фото
class Comment(Base):
    """Класс модели Comment,
    который наследуется от базового класса Base"""
    __tablename__ = 'comments' # Указание имени таблицы в базе данных.

    id = Column(Integer, primary_key=True, index=True)
    photo_id = Column(Integer, ForeignKey('photos.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(Text, nullable=False)
    user = relationship("CustomUser", back_populates="comments")
    photo = relationship("Photo", back_populates="comments")

"""Эти строки добавляют связи между моделями, 
которые были объявлены без обратных связей"""
CustomUser.photos = relationship("Photo", back_populates="user")
CustomUser.comments = relationship("Comment", back_populates="user")
Photo.comments = relationship("Comment", back_populates="photo")
