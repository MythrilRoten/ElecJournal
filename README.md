# ElecJournal
***
## 1. Установка git


Выбираете там виндовс и везде нажимаете да ~~(насколько я помню)~~
> [Git](https://git-scm.com/downloads "Ссылка на скачивание")


## 2. Установка репозитория
Выбираете папку где хотите чтоб был расположен сайт и нажимаете "Открыть в терминале", или в cmd прописываете путь, и далее там же в cmd прописываете
> ``git clone https://github.com/MythrilRoten/ElecJournal.git``

## 3. Создание виртуального окружения ~~(для чего оно вы и сами можете почитать)~~
1. Установка пакета
> ``pip install virtualenv``

2. Пишем эту команду в папке с сайтом
> ``python -m venv НазваниеОкружения``

3. Активируем окружение
> ``НазваниеОкружения\Scripts\activate.bat`` - **для Windows**

> ``source НазваниеОкружения/bin/activate`` - **для Linux и MacOS**

4. Установка пакетов для сайта
> ``pip install -r requirements.txt

## 4. Кодим

##

pip freeze > requirements.txt

