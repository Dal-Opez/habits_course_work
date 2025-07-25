# habits_course_work

Проект реализовывает трекер привычек. Пользователь имеет возможность записывать свои привычки, напоминание о которых
происходит путем рассылки через телеграм бота

## 🛠 Технологии
- Python 3.11
- Django 5.5.0
- PostgreSQL
- Redis
- Celery
- Nginx
- Docker + Docker Compose
- GitHub Actions (CI/CD)

## 🚀 Запуск проекта

### Локальная разработка (с Docker)

1. Склонируйте репозиторий:
   ```bash
   git clone git@github.com:Dal-Opez/habits_course_work.git
   ```
2. Создайте файл .env в корне проекта (пример в .env.example):
   ```
    SECRET_KEY=<ваш-secret-key>
    POSTGRES_DB=<имя-бд>
    POSTGRES_USER=<пользователь-бд>
    POSTGRES_PASSWORD=<пароль-бд>
    # Остальные переменные...
   ```
3. Запустите сервисы:
```
docker-compose up -d
```
4. Примените миграции:
```
docker-compose exec web python manage.py migrate
```
5. Создайте суперпользователя (опционально):
```
docker-compose exec web python manage.py migrate
```
6. Проект доступен по адресу:
```
http://localhost:8000
```

## ☁️ Деплой на сервер

### Требования к серверу
Ubuntu 22.04 LTS

Установленные Docker и Docker Compose

### Инструкция по настройке сервера
1. Установите Docker:
```
sudo apt-get update && sudo apt-get install docker.io docker-compose-plugin
```
2. Установите фаервол:
```
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
sudo ufw enable
```
3. Добавьте пользователя в группу docker:
```
sudo usermod -aG docker $USER
```

### Настройка CI/CD
1. В GitHub Secrets (Settings → Secrets and variables → Actions) добавьте:

Добавьте secrets в GitHub (Settings → Secrets and variables → Actions):

+ DOCKER_HUB_USERNAME — логин Docker Hub

+ DOCKER_HUB_TOKEN — токен доступа

+ DEPLOY_SSH_KEY — приватный SSH-ключ для доступа к серверу

+ DEPLOY_SSH_USER — пользователь сервера (обычно root или ubuntu)

+ DEPLOY_SERVER_IP — IP сервера (158.160.193.173)

+ DJANGO_SECRET_KEY - секретный ключ Django

+ TELEGRAM_BOT_TOKEN - токен Telegram-бота


2. Workflow автоматически выполнит:
+ Тестирование и линтинг

+ Сборку Docker-образов

+ Деплой на сервер при пуше в main