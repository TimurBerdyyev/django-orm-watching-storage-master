# Описание проекта "Управление доступом в хранилище"
Этот проект представляет собой внутренний репозиторий для сотрудников хранилища. Он предоставляет интерфейс для управления доступом и отслеживания посещений сотрудников.

### Зачем это нужно
Пульт управления доступом в хранилище предназначен для обеспечения безопасности и контроля доступа в хранилище. Он позволяет управлять пропусками сотрудников, отслеживать их посещения и получать информацию о текущем состоянии хранилища.
### Как это работает
Проект состоит из нескольких модулей:
1. Модели данных: Включает модели Passcard и Visit, которые представляют собой информацию о пропусках сотрудников и их посещениях.
2. Представления Django: Включает представления для отображения активных пропусков, информации о посещениях и других функций управления доступом.
3. Шаблоны HTML: Содержат шаблоны для отображения данных и взаимодействия с пользователем
4. Файлы статики: Включают CSS-файлы и другие ресурсы, необходимые для оформления и работы интерфейса.
### Как установить
Клонируйте данный репозиторий на свой компьютер командой `git clone https://github.com/TimurBerdyyev/django-orm-watching-storage.git`
Убедитесь, что у вас установлен Python и Django.
Установите зависимости, выполнив команду `pip install -r requirements.txt`

## Инструкция по настройке окружения
Этот репозиторий содержит проект, который использует базу данных PostgreSQL для хранения данных. Проект разработан для работы с сайтом по контролю доступа.
1. Создание файла `.env` далее в этот файл вы должны прописать
2. `DATABASE_URL`: URL для подключения к базе данных PostgreSQL. Пример: `postgresql://user:password@host:port/name`.
3. `SECRET_KEY`: Секретный ключ, используемый для шифрования паролей пользователей сайта.
4. `ALLOWED_HOSTS`: Список разрешенных хостов, которые могут обращаться к вашему сайту.
5. `DEBUG_KEY`: Установить значение `False` для отключения режима отладки.

Далее запускаем проект командой `python manage.py runserver` , посде переходим по указоному адресу 






