# Good Habits

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
SECRET_KEY=секретный ключ Django
POSTGRES_DB=название базы данных (habits)
POSTGRES_USER=имя пользователя (postgres)
POSTGRES_PASSWORD=пароль
POSTGRES_HOST=хост (localhost) 
POSTGRES_PORT=5432
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
TELEGRAM_BOT_API_KEY=токен для обращения к API Telegram-бота

# через Docker
POSTGRES_HOST = db
CELERY_BROKER_URL="redis://redis:6379/0"
CELERY_RESULT_BACKEND="redis://redis:6379/0"
```
*В проекте есть шаблон файла .env - `.env_example`

### Шаг 6: Применение миграций
Выполнить команду
```bash
python manage.py migrate
```
### Шаг 7: Создание суперпользователя
! Использовать только для admin !
Выполнить команду
```bash
python manage.py csu
```

### Шаг 8: Установка и настройка Redis
1. Установить
```bash
brew install redis
```
2. Запустить в отдельном окне терминала 
```bash
redis-server
```
### Шаг 9: Запуск celery
1. Открыть новое окно терминала
2. Из каталога проекта запустить celery командой
```bash
celery -A config worker -l info
```
### Шаг 10: Запуск celery-beat
1. Открыть новое окно терминала
2. Из каталога проекта запустить celery командой
```bash
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
### Шаг 11: Запуск сервера Django
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
### Результат покрытия тестами лежит в корне проекта
```bash
 coverage_result.png
```


## Работа с проектом с помощью Docker

1. Выполнить Шаги 1 и 5 Подготовки к проекту
2. Чтобы создать образ и запустить проект, выполнить команду в терминале
```bash
docker-compose up --build  
```
3. Создание суперпользователя
! Использовать только для admin !
```bash
docker-compose exec app python3 manage.py csu
```
4. Запуск тестов 
```bash
docker-compose exec app coverage3 run --source='.' manage.py test
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


### Эндпоинты:
1) Создание привычки
```bash
POST: http://localhost:8000/habits/create/
body: {
    "related_habit": null,
    "place": "Дом",
    "time": "19:51:00",
    "action": "Приседания",
    "is_pleasant": true,
    "periodicity": 1,
    "reward": null,
    "time_to_complete": "00:01:30", 
    "is_public": false
  } 
  
      *related_habit, reward, is_public - необязательны для заполнения 
```
2) Просмотр детальной информации о привычке
```bash
GET: http://localhost:8000/habits/<id_привычки>/
```
3) Просмотр всех привычек
```bash
GET: http://localhost:8000/habits/
```
4) Просмотр публичных привычек
```bash
GET: http://localhost:8000/habits/public/
```
5) Редактирование привычки
```bash
PUT: http://localhost:8000/habits/<id_привычки>/
PATCH: http://localhost:8000/habits/<id_привычки>/
```
6) Удаление привычки
```bash
DELETE: http://localhost:8000/habits/<id_привычки>/
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
## Просмотр документации c помощью Docker
### Swagger
```bash
http://localhost:8000/swagger/
```
### Redoc
```bash
http://localhost:8000/redoc/
```