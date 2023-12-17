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
TELEGRAM_BOT_API_KEY=токен для обращения к API Telegram-сервисов

```
*В проекте есть шаблон файла .env - `.env_example`

### Шаг 6: Применение миграций
1. Выполнить команду
```bash
python manage.py migrate
```

