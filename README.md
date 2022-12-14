## Задание для хакатона от ВТБ по data треку

Перед началом работы, надо установить зависимости и создать виртуальное окружения для работы, при помощи этих команд в папке проекта
```shell
python -m venv venv
pip install -r requirements.txt
pip install pandas
pip install sklearn
pip install schedule
pip install pyTelegramBotApi
```
### Парсинг данных (не обязательно. собранный датафрейм и обученная модель уже есть в файлах проекта)
В папке parser находятся файлы для создания csv файла. Для запуска надо перейти в директорию командой 
```shell
cd parser
```
Потом запускаем файл parsing.py командой и ждем ее окончания
```shell
python parsing.py
```
Будет создан csv_file.csv с новостями
### Обучение модели
Дальше нужно обучить модель. После обучения нужно запустить телеграм бота.  (Модель сама обучиться автоматически, если вы не сделаете этого вручную)
### Запуск телеграм бота
Из корневого каталога проекта, запускается команда
```shell
python bot.py
```
После запуска бота, нужно открыть его и начать с ним диалог при помощи команды /start. Можно запросить как инсайты и тренды, так и новости

### Пример работы бота

начало рабюоты с ботом: 
![alt text](./images/Начало_работы_с_ботом.png "start_bot")

Вывод новостей: 
![alt text](./images/Вывод_новостей.png "news")

Вывод инсайтов: 
![alt text](./images/Вывод_инсайтов.png "insites")




### Авторы:

Ксения Матвеева: data analyst, генератор идей

Дарья Матвеева: backend, data science, фундамент команды, самый азартный игрок

Павел Ломоносов: самый надежный backend
