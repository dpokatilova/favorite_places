Улюблені місця

Інструкція до запуску:
1. Клонувати репозиторій:
    git clone
    cd My_favorite_places
2. Створити та активувати віртуальне оточення:
   На Windows:
   python -m venv .venv
   .venv\Scripts\activate
   На macOS / Linux:
   python3 -m venv .venv
   source .venv/bin/activate
3. Встановити залежності:
   pip install -r requirements.txt
4. Застосувати міграції:
   python manage.py migrate
5. Запустити локальний сервер:
   python manage.py runserver
6. Відкрити в браузері:
   http://127.0.0.1:8000/