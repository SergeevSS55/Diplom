from pydantic import BaseModel
from datetime import date
from typing import Optional
from typing import List

"""Этот модуль играет ключевую роль в управлении и валидации данных.
Если данные не соответствуют схеме данных, FastAPI вернет ошибку"""


class UserBase(BaseModel):
    """Базовая модель для представления пользователя с параметрами:
    username, first_name, last_name, email,
    phone_number (необязательное), birth_date (необязательное)"""
    username: str
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    birth_date: Optional[date] = None


class UserCreate(UserBase):
    """Модель для создания нового пользователя.
    Добавляет обязательное поле password"""
    password: str


class User(UserBase):
    """Модель с идентифицирующим номером пользователя"""
    id: int

    class Config:
        """Настройка поведения Pydantic при взаимодействии с моделями"""
        orm_mode = True


class PhotoBase(BaseModel):
    """Базовая модель для представления фотографий"""
    filename: str
    description: Optional[str] = None


class PhotoCreate(PhotoBase):
    """Модель для создания новой фотографии"""
    pass


class Photo(PhotoBase):
    """Модель для представления фотографии.
    Список комментариев к фотографии связан с моделью Comment"""
    id: int
    user_id: int
    comments: List["Comment"] = []

    class Config:
        """Настройка поведения Pydantic при взаимодействии с моделями"""
        orm_mode = True


# Схемы для комментариев
class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    photo_id: int
    user_id: int

    class Config:
        orm_mode = True
