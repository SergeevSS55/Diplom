from fastapi import FastAPI, Depends, HTTPException, Form, Request, status, File, UploadFile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from bookface import models, crud, schemas, forms
import os
from fastapi.staticfiles import StaticFiles

"""Настройка базы данных и создание движка SQLAlchemy,
который используется для подключения и взаимодействия с базой данных"""
DATABASE_URL = "sqlite:///ecomerce.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Движок для взаимодействия с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)  # Создание таблиц, описанных в моделях

app = FastAPI()  # Создаем экземпляр приложения FastAPI
templates = Jinja2Templates(directory="bookface/templates")  # Настройка шаблонизатора Jinja2 и установка пути

UPLOAD_DIR = "uploads"  # Директория для хранения загруженных файлов
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


def get_db():
    """Генератор для управления сессиями базы данных"""
    db = SessionLocal()  # Создание новой сессии БД
    try:
        yield db
    finally:
        db.close()


# Главная страница
@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Этот декоратор регистрирует функцию home
    как обработчик GET-запросов для URL (/).
    Возвращает преобразованный HTML-шаблон"""
    return templates.TemplateResponse("home.html", {"request": request})


# Регистрация нового пользователя
@app.get("/reg", response_class=HTMLResponse)
async def register_form(request: Request) -> HTMLResponse:
    """GET-запрос на URL-адрес /reg.
    Преобразовывает страницу для регистрации пользователя"""
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/reg")
async def register_user(request: Request, db: Session = Depends(get_db)):
    """Обработка отправки форм регистрации.
    В случае успешной регистрации возвращается словарь
    {"message": "User registered successfully"}."""
    form_data = await request.form()  # Приостановление работы до получения данных
    user_data = forms.UserRegistrationForm(
        username=form_data.get("username"),
        first_name=form_data.get("first_name"),
        last_name=form_data.get("last_name"),
        email=form_data.get("email"),
        phone_number=form_data.get("phone_number"),
        birth_date=form_data.get("birth_date"),
        password=form_data.get("password"),
        confirm_password=form_data.get("confirm_password"),
    )  # Передача значений, извлеченных из формы UserRegistrationForm

    user_data.check_passwords()  # Вызываем метод на проверку пароля из класса UserRegistrationForm

    user = schemas.UserCreate(**user_data.dict())
    crud.create_user(db, user)  # Вызываем метод create_user для создания нового пользователя
    return {"message": "User registered successfully"}


# Список пользователей
@app.get("/list", response_class=HTMLResponse)
async def users_list(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    """Обработка Гет-запроса на получение списка, зарегестрированных пользователей.
    Возвращает список пользователей из базы данных"""
    users = crud.get_users(db)  # Вызываем функцию для извлечения всех пользователей
    return templates.TemplateResponse("users_list.html", {"request": request, "users": users})


@app.get("/photos", response_class=HTMLResponse)
async def view_photos(request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    """Обработка Гет-запроса на получение списка фотографий.
        Возвращает список фотографий из базы данных"""
    photos = crud.get_photos(db)  # Вызываем функцию для извлечения всех фотографий
    current_user = {"id": 1, "username": "test_user"}  # Временно передаем фиктивного пользователя
    return templates.TemplateResponse(
        "photos.html",
        {"request": request, "photos": photos, "current_user": current_user}
    )


@app.post("/upload_photo")
async def upload_photo(file: UploadFile, db: Session = Depends(get_db)):
    """Асинхронная функция-обработчик для запросов к эндпоинту "/upload_photo".
    Получает загруженный файл из данных формы и сессию базы данных."""
    file_path = os.path.join(UPLOAD_DIR, file.filename)  # Создаем путь для сохранения фотографий
    with open(file_path, "wb") as f:  # Считываем содержимое открытого файла и записываем данные в открытый файл
        f.write(await file.read())

    photo = models.Photo(filename=file.filename)  # Создается экземпляр модели Photo
    db.add(photo)
    db.commit()
    db.refresh(photo)
    return {"photo_id": photo.id, "message": "Photo uploaded successfully"}


@app.post("/photos/{photo_id}/comments")
async def add_comment(
        photo_id: int,
        text: str = Form(...),  # Получаем текст комментария из формы
        user_id: int = Form(...),  # ID пользователя также передаётся через форму
        db: Session = Depends(get_db),
):
    """Асинхронная функция-обработчик для запросов к эндпоинту /photos/{photo_id}/comments.
     Получает ID фотографии, к которой будет добавлен комментарий,
     ID пользователя, который добавляет комментарий, сессию БД, текст комментариев.
     Возвращает словарь об успешной загрузке комментария."""
    comment_data = schemas.CommentCreate(text=text)
    # Передаем в функцию add_comment новый комментарий
    comment = crud.add_comment(db, comment_data, user_id=user_id, photo_id=photo_id)
    return {"comment_id": comment.id, "message": "Comment added successfully"}
