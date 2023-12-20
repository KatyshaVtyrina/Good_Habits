# Online Education

## Описание

SPA-приложение - трекер полезных привычек

## Данные

**Cущности проекта:**

- Пользователи
- Привычки


## Подготовка к работе с проектом

### Шаг 1: Клонирование проекта
1. Зайти в терминал
2. С помощью команды `cd` перейти в директорию, где будет находиться проект
3. Клонировать проект
```bash
git clone https://github.com/KatyshaVtyrina/Good_Habits.git
```

### Шаг 2: Настройка виртуального окружения

1. Создать виртуальное окружение
```bash
python3 -m venv venv
```
2. Активировать виртуальное окружение
```bash
source venv/bin/activate
```

### Шаг 3: Установка зависимостей
1. Перейти в каталог проекта
```bash
cd Good_Habits
```
2. Установить зависимости проекта из файла`requirements.txt`
```bash
pip install -r requirements.txt
```

### Шаг 4: Установка и настройка PostgreSQL
1. Установить PostreSQL
```bash
brew install postgres
```
2. Подключиться к PostgreSQL от имени пользователя postgres
```bash
psql -U postgres 
```
3. Создать базу данных `habits`
```bash
CREATE DATABASE habits;
```
4. Выйти
```bash
\q
```

### Шаг 5: Настройка окружения
1. В директории проекта создать файл `.env`

3. Записать в файл следующие настройки
```bash
DB_USER=имя пользователя (postgres)
DB_PASSWORD=пароль
DB_NAME=название базы данных (habits)
SECRET_KEY=секретный ключ
TELEGRAM_BOT_API_KEY=токен для обращения к API Telegram-бота

```
*В проекте есть шаблон файла .env - `.env_example`

### Шаг 6: Применение миграций
Выполнить команду
```bash
python manage.py migrate
```

### Шаг 7: Установка и настройка Redis
1. Установить
```bash
brew install redis
```
2. Запустить в отдельном окне терминала 
```bash
redis-server
```
### Шаг 8: Запуск celery
1. Открыть новое окно терминала
2. Из каталога проекта запустить celery командой
```bash
celery -A config worker -l info
```
### Шаг 9: Запуск celery-beat
1. Открыть новое окно терминала
2. Из каталога проекта запустить celery командой
```bash
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
### Шаг 10: Запуск сервера Django
1. Открыть новое окно терминала

2. Запустить сервер
```bash
python manage.py runserver
```

## Запуск тестов

### Для запуска тестов выполнить команду
```bash
 coverage3 run --source='.' manage.py test
```

## Просмотр документации
### Swagger
```bash
http://127.0.0.1:8000/swagger/
```
### Redoc
```bash
http://127.0.0.1:8000/redoc/
```
## Работа с сервисом через Postman

1. Зарегистрироваться
```bash
POST: http://localhost:8000/users/register/
body: {
  "email": <электронная почта>,
  "password": <пароль>,
  "tg_id": <телеграмм id>
  }
```

2. Получить токен
```bash
POST: http://localhost:8000/users/token/
body: {
  "email": <электронная почта>,
  "password": <пароль>
  }
```

3. Подключить авторизацию по токену

4. Создать привычку
```bash
POST: http://localhost:8000/habits/create/
body: {
    "place": "Дом",
    "time": "19:51:00",
    "action": "Приседания",
    "is_pleasant": true,
    "periodicity": 1,
    "time_to_complete": "00:01:30"
  } 
```


