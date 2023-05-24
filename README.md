# api_final
## Описание
Наворачиваем возможность работать с Yatube посредством API!!

## Задействованные технологии
Django==3.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0

## Инструкция по запуску
- Склонируйте репозиторий в локальное хранилище:
```
git clone <repository_link>
```
- Создайте и активируйте виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
- Обновите пакетный менеджер до последней версии:
```
pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
- Сформируйте и проведите миграции из папки, содержащей manage.py
```
python manage.py makemigrations
python manage.py migrate
```
- Проект можно запускать следующей командой:
```
python manage.py runserver
```