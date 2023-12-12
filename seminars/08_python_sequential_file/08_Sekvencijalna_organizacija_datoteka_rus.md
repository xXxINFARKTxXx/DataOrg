 ## Факультет технических наук, ДРА, Нови Сад

## Предмет:

## Организация данных

```
д-р Владимир Иванчевич
Никола Тодорович
Владимир Йованович
```

# Последовательная организация

# файла


# Последовательный файл

- Основная структура
    - записи расположены последовательно одна за другой
    - логически соседние записи размещаются в физически
       соседних местах
          - имеется информация о связях между записями логической
             структуры данных файла, встроенная в физическую
             структуру
          - реализована как линейная логическая структура данных
             - помещением записи с более высоким значением ключа в
                место с более высоким адресом


# Последовательный файл

- Основная структура
    - логически соседние записи размещаются в физически
       соседних местах
          - упорядочивание по значениям ключа в порядке
             возрастания -> запись с наименьшим значением ключа
             помещается на первое место
    - также известен как физическая последовательная организация


# Последовательный файл

- Основная структура
    - связь между сохраненными значениями ключа
       k(S) и адресами местоположения
          - не встроена в структуру файла
          - не представляет собой какую-либо математическую функцию
    - записи размещаются блоками по _f_ записей
       - желательно, чтобы фактор блокировки _f_ был как можно больше


# Последовательный файл

- Основная структура
    - современные ОС ( _Unix_ ) и языки программирования ( _C_ , _C++_ ,
       _Java_ ) поддерживают только последовательный способ
       доступа
          - пользователям предоставляется возможность создавать свои
             собственные последовательные методы доступа


# Последовательный файл

- Пример последовательного

### файла


# Задача 1

- Написать программу, которая будет работать с

#### данными о зарегистрированных прибытиях заключенных

#### в городскую тюрьму. Для каждого поступления нового

#### заключенного в последовательном файле с фактором

#### блокировки f = 4 регистрируются:

- регистрационный номер (до 8 цифр)
- код заключенного (ровно 7 символов)
- дата и время прибытия
- обозначение ячейки, в которую заключенный будет помещен (ровно 5
    символов)
- продолжительность наказания в месяцах (до 480 месяцев)


# Задача 1

- Реализовать:
    - формирование файла
    - ввод новой записи
    - обновление записи
    - удаление записи
       - логическое
    - поиск по ключу
    - реорганизация файла
    - вывод всех записей

# Задача 2

- Реализовать последовательный файл, в котором

### записи вводятся с использованием последовательного

### файла изменений.

- Все ошибки, возникающие во время работы
    программы, должны быть помещены в файл ошибок


# Задача 3

- Реализовать последовательный файл, параметры которого

### (фактор блокировки, наличие

### последовательного файла изменений, пути к

### файлам) задаются с помощью отдельной

### программы. После задания этих параметров,

### последовательный файл должен автоматически

### функционировать с указанными параметрами.