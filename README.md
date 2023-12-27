# online-platform-of-the-electronics-trading-network
онлайн платформа торговой сети электроники
Использованные технологии:
Python 3.8+
Django 3+
DRF 3.10+
PostgreSQL 10+

Запуск прокта 
1. Заполните переменные окружения в файле .evg. Пример файла .env.sample
2. Создайте виртуальное окружение python3 -m venv env
3. Установите используемые библиотеки pip install -r requirements.txt
4. Создайте миграции в базе данных с помощью python3 manage.py makemigrations; python3 manage.py migrate
5. Запустите приложение python3 manage.py runserver
