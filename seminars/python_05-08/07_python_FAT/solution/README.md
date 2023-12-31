# Организация данных
## Инженерия программного обеспечения и информационные технологии
### Организация файлов в языке программирования Python

#### Предпосылки для запуска
- Python 3.7+ [скачать](https://www.python.org/downloads/)
- Текстовый редактор по вашему выбору

#### Инструкции по запуску
1. Скачайте (или клонируйте) репозиторий.
2. Откройте командную строку (терминал, gitbash, powershell или что-то еще).
3. Запустите `main.py` сценарий с помощью команды `python main.py`.

#### Описание примера
Работа со слотами реализована с использованием библиотеки [struct](https://docs.python.org/3/library/struct.html), которая предоставляет возможность работы со структурами, аналогично языку программирования C.
В примере используется **struct** со следующими характеристиками:
- *id* - целое число,
- *name* - строка длиной 10,
- *q* - вещественное число,
- *status* - целое число.

Названия этих атрибутов определены в `constrants.py`.
Сразу после списка атрибутов определен формат упаковки байтов: `i` - integer, `10s` - строка длиной 10, `d` - double.
Любое изменение атрибута подразумевает применение этой строки формата.
Список символов форматирования для всех примитивных типов данных доступен [здесь](https://docs.python.org/3/library/struct.html#format-characters).

Вместо ручной загрузки, данные считываются из специального текстового файла `data/in.txt` и записываются в бинарный файл.
В настоящее время поддерживаются следующие типы организации файлов:
- Серийная (`serial_file.py`),
- Последовательная (`sequential_file.py`), и
- Рассеянная с серийной зоной переполнения(`hash_file.py`).

Выбор организации осуществляется путем раскомментирования создания желаемого типа файла в `main.py`, в то время как остальные два остаются закомментированными.
В `binary_file.py` определен абстрактный класс `BinaryFile`, который затем наследуется и конкретизируется в `serial_file.py`, `sequential_file.py` и `hash_file.py`.
Упаковка структур в массив байтов и обратные операции реализованы в `record.py`.