from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

"""Модуль реализует логику работы базы данных для дальнейшего включения в обработку запросов.
Использование готовых данных из модулей models, schemas и их синхронизация"""

"""Создание объекта для хэширования пароля"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: schemas.UserCreate):
    """Функция для создания нового пользователя.
    Принимает сессию базы данных, объект с данными пользователя,
    который соответствует Pydantic схеме UserCreate из модуля schemas.
    Возвращает созданного пользователя"""
    hashed_password = pwd_context.hash(user.password)  # Хэширование пароля
    db_user = models.CustomUser(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        phone_number=user.phone_number,
        birth_date=user.birth_date,
        hashed_password=hashed_password,
    )  # Создание нового объекта модели, заполняя данными схемы UserCreate из модуля schemas
    db.add(db_user)  # Добавление объекта
    db.commit()  # Сохранение изменений в БД
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Функция для получения списка пользователей.
    Принимает сессию базы данных, параметр, указывающий,
    сколько пользователей пропустить (для пагинации),
    параметр, указывающий, сколько пользователей вернуть.
    Возвращает список пользователей, запрошенных из базы данных
    с учетом параметров пропуска и лимита"""
    return db.query(models.CustomUser).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    """Функция для получения пользователя по имени пользователя"""
    return db.query(models.CustomUser).filter(models.CustomUser.username == username).first()


def add_photo(db: Session, photo: schemas.PhotoCreate, user_id: int):
    """Функция для добавления фотографии. Принимает сессию базы данных,
    объект с данными фото, который соответствует Pydantic схеме PhotoCreate из модуля schemas,
    ID пользователя, добавившего фото.
    Возвращает добавленное фото"""
    db_photo = models.Photo(**photo.dict(), user_id=user_id)  # Создание объект модели Photo на основе схемы PhotoCreate
    db.add(db_photo)  # Добавление объекта
    db.commit()
    db.refresh(db_photo)
    return db_photo


def get_photos(db: Session, skip: int = 0, limit: int = 100):
    """Функция для получения списка фотографий.
    Возвращает список фотографий, запрошенных из базы данных
    с учетом параметров пропуска и лимита."""
    return db.query(models.Photo).offset(skip).limit(limit).all()


def add_comment(db: Session, comment: schemas.CommentCreate, user_id: int, photo_id: int):
    """Функция для добавления комментария.
    Принимает сессию базы данных, объект с данными комментария,
    который соответствует Pydantic схеме CommentCreate из модуля schemas,
    ID пользователя, оставившего комментарий,
    ID фотографии, к которой добавляется комментарий.
    Возвращает сохраненный объект комментария"""
    db_comment = models.Comment(**comment.dict(), user_id=user_id, photo_id=photo_id)
    # Создает объект модели Comment на основе данных из схемы CommentCreate, user_id и photo_id
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments_by_photo(db: Session, photo_id: int):
    """Функция для получения списка комментариев к фотографии.
    Возвращает список комментариев к фотографии"""
    return db.query(models.Comment).filter(models.Comment.photo_id == photo_id).all()
