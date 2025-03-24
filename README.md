

Пример работы приложения на Flask с привязкой к базе данных:
Демоснтрация основной страницы приложения.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20main.png)

Страница с изображением полей для регистрации нового пользователя.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20reg.png)

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20reg_new.png)

Список пользователей - это страница с изображением всех зарегестрированных пользователей с привязкой к базе данных.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20user_list.png)

Галерея фотографий. На данной странице есть вкладка для загрузки фотографий, а также список ранее загруженных фотографий пользователями.
Данную страницу могут посетить только зарегестрированные прльзователи. (Демонстрация вместе с БД).

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20photo_list.png)

Рядом с картинкой можно просмотреть оставленные комментарии
Как и с предыдущей страницей - доступна для зарегестрированных пользователей.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20comment.png)

Добавление новой фотографии и ее появление в списке картинок

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20photo_upload.png)


![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/Flask_%20new_photo.png)


Созданные таблицы через Alembic

![image](https://github.com/SergeevSS55/Diplom/blob/main/Flusk_images/2024-12-23_20-52-25.png)

### **FastAPI**

Пример работы приложения на FastAPI с привязкой к базе данных:
Демоснтрация основной страницы приложения.

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20main.png)

Страница с изображением полей для регистрации нового пользователя.

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20reg.png)

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20reg_new.png)

Сообщение об успешной загрузке пользователя

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20user_dict.png)

Список пользователей - это страница с изображением всех зарегестрированных пользователей с привязкой к базе данных.

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20user_list.png)

Галерея фотографий. На данной странице есть вкладка для загрузки фотографий, а также список ранее загруженных фотографий пользователями.
Данную страницу могут посетить только зарегестрированные прльзователи. (Демонстрация вместе с БД).

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20galery.png)

Сообщение об успешной загрузке фотографии

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20photo_dict.png)

Рядом с картинкой можно просмотреть оставленные комментарии
Как и с предыдущей страницей - доступна для зарегестрированных пользователей.

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_%20comments.png)

Созданные таблицы через Alembic

![image](https://github.com/SergeevSS55/Diplom/blob/main/FastAPI_images/Fast_API_db.png)


### **Django**

Пример работы приложения на Django с привязкой к базе данных:
Демоснтрация основной страницы приложения.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_app_work%20(2).png)

Страница с зображением полей для регистрации нового пользователя.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_app_work%20(1).png)

Список пользователей - это страница с изображением всех зарегестрированных пользователей с привязкой к базе данных.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_DB%20(2).png)

Галерея фотографий. На данной странице есть вкладка для загрузки фотографий, а также список ранее загруженных фотографий пользователями.
Данную страницу могут посетить только зарегестрированные прльзователи. (Демонстрация вместе с БД).

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_DB%20(3).png)

При нажатии на картинку, переходим на адрес соответсвующей картинки, где можно просмотреть оставленные пользователями комментарии.
Как и с предыдущей страницей - доступна для зарегестрированных пользователей.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_DB%20(4).png)

Страница для загрузки фотографий.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_uploading_photo.png)

Джанго-таблицы и созданные нами таблицы.

![image](https://github.com/SergeevSS55/Diplom/blob/main/Django_photo/dj_DB%20(1).png)


## Приложение 1. Пример файловой структуры

flaskDiplom
├── .venv
├── app.py
├── models.py
├── forms.py
├── config.py
├── requirements.txt
├── migrations/
│     ├── env.py
│     ├── alembic.ini
│     ├── script.py.mako
│     └── versions/
│         └── migration_name.py
|
├── templates/
|     ├── home.html
|     ├── register.html
|     ├── login.html
|     ├── photos.html
|     └── users_list.html
|
├── uploads
|
├── instance
|     └── db.sqlight3


FastAPIDiplom
  ├── .venv
  |
  ├── bookface
  |     ├── __init.py__
  │     ├── forms.py
  │     ├── models.py
  │     ├── main.py
  │     ├── schemas.py
  |     ├── crud.py
  │     ├── templates/
  |     |     ├── home.html
  |     |     ├── register.html
  |     |     ├── photos.html
  |     |     ├── get_photo.html
  |     |     └── users_list.html
  |     |
  |     ├── migrations/
  │           ├── env.py
  │           ├── README
  │           ├── script.py.mako
  │           └── versions/
  │                 └── migration_name.py          
  |
  ├── uploads
  |
  ├── alembic.ini
  |
  ├── ecomerce.db
  |
  └── requirements.txt


djangoProject
 ├── .venv
 |
 ├── reqs.txt
 |
 ├── SocialNetwork
 |    |
 |    ├── manage.py
 |    |
 |    └── SocialNetwork
 |         ├── __init__.py
 |         ├── asgi.py
 |         ├── settings.py
 |         ├── urls.py
 |         └── wsgi.py
 |
 ├── bookface
 |      ├── __init__.py
 |      ├── admin.py
 |      ├── apps.py
 |      ├── models.py
 |      ├── tests.py
 |      ├── views.py
 |      └── migrations
 |           ├── 0001_initial.py
 |           └── __init__.py
 |
 ├── media
 |     └── photo
 |
 ├── static
 |     └── style.css
 |
 ├── templates
 |      ├── home.html
 |      ├── photo_detail.html
 |      ├── photo_gallery.html
 |      ├── register.html
 |      ├── upload_photo.html
 |      └── users_list.html
 |
 └── db.sqlite3

## Приложение 2. Список необходимых библиотек
### **Flаsk**
﻿alembic==1.14.0
blinker==1.9.0
click==8.1.7
colorama==0.4.6
dnspython==2.7.0
email_validator==2.2.0
Flask==3.1.0
Flask-Login==0.6.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.6
MarkupSafe==3.0.2
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3
WTForms==3.2.1

### **FastAPI**
﻿alembic==1.14.0
annotated-types==0.7.0
anyio==4.6.2.post1
bcrypt==4.2.0
click==8.1.7
colorama==0.4.6
ecdsa==0.19.0
fastapi==0.115.5
greenlet==3.1.1
h11==0.14.0
idna==3.10
Jinja2==3.1.4
Mako==1.3.6
MarkupSafe==3.0.2
passlib==1.7.4
pyasn1==0.6.1
pydantic==2.9.2
pydantic_core==2.23.4
python-jose==3.3.0
python-multipart==0.0.17
rsa==4.9
six==1.16.0
sniffio==1.3.1
SQLAlchemy==2.0.36
starlette==0.41.2
typing_extensions==4.12.2
uvicorn==0.32.0

### **Django**
﻿asgiref==3.8.1
Django==5.1.4
sqlparse==0.5.3
tzdata==2024.2
