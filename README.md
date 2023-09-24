# Онлайн Банк Pet-Проект

## Описание проекта
Этот pet-проект представляет собой онлайн банк, реализованный с использованием фреймворка Django. Проект позволяет пользователям выполнять различные банковские операции, такие как переводы и пополнение баланса. Проект также включает в себя систему регистрации и аутентификации пользователей. Однако, одной из главных особенностей проекта является наличие страницы с текущими курсами валют, которая обновляется в фоновом режиме через API сайта ЦБ РФ.

## Основные функциональности
1. **Регистрация**: Пользователи могут зарегистрировать аккаунт в системе, предоставив необходимые персональные данные. Поддерживается вход в аккаунт, смена пароля, а также восстановление пароля.

2. **Пополнение баланса**: Зарегистрированные пользователи могут пополнять свой баланс.

3. **Переводы**: Пользователи могут осуществлять денежные переводы другим пользователям внутри системы. Это включает в себя указание суммы перевода и получателя.

4. **Страница с курсами валют**: Система обновляет текущие курсы валют через API сайта ЦБ РФ. Пользователи могут просматривать актуальные курсы валют.

5. **Технологии**: Для реализации проекта были использованы технологии RabbitMQ и Dramatiq. RabbitMQ используется для обеспечения асинхронной коммуникации между компонентами системы, а Dramatiq позволяет легко управлять задачами в фоновом режиме и обработкой событий. Frontend релизован с использованием Bulma

## Требования к окружению
Для успешного запуска проекта необходимо наличие следующего окружения:

- Python (версия 3.11+)
- RabbitMQ (для обеспечения очереди сообщений)
- База данных (например, Sqlite)

## Установка и запуск
1. Установите необходимые зависимости.
2. Убедитесь, что запущен сервер RabbitMQ.
3. Запустите сервер командой py manage.py runserver
4. Запустите скрипты в отдельных терминалах: dramatiq exchange_currency.tasks -p 1 и py tasks.py

# Online Bank Pet Project

## Project Description
This pet project is an online bank implemented using the Django framework. The project allows users to perform various banking operations such as transfers and balance replenishment. The project also includes a user registration and authentication system. However, one of the main features of the project is the presence of a page with current currency exchange rates, which is updated in the background through the API of the Central Bank of Russia.

## Key Features
1. **Registration**: Users can register an account in the system by providing the necessary personal information. Account login, password change, and password recovery are supported.

2. **Balance Replenishment**: Registered users can replenish their balance.

3. **Transfers**: Users can make monetary transfers to other users within the system. This includes specifying the transfer amount and recipient.

4. **Currency Exchange Rates Page**: The system updates current currency exchange rates through the Central Bank of Russia's API. Users can view up-to-date currency exchange rates.

5. **Technologies**: RabbitMQ and Dramatiq technologies were used to implement the project. RabbitMQ is used to provide asynchronous communication between system components, and Dramatiq allows easy management of background tasks and event processing. The frontend is implemented using Bulma.

## Environment Requirements
To successfully run the project, the following environment is required:

- Python (version 3.11+)
- RabbitMQ (for message queuing)
- Database (e.g., Sqlite)

## Installation and Running
1. Install the necessary dependencies.
2. Ensure that the RabbitMQ server is running.
3. Start the server with the command `py manage.py runserver`.
4. Run the scripts in separate terminals: `dramatiq exchange_currency.tasks -p 1` and `py tasks.py`.

