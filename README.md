# Читабельный JSON

Выводит содержимое `JSON файла` в консоль в удобном для чтения виде. С отступами, переносами и пробелами.

### Пример

Стандартный вывод:
```json
[{"global_id":1699129,"DepartmentalAffiliation":"Департамент жилищно-коммунального хозяйства города Москвы","ID":1,"ClarificationOfWorkingHours":"Посещение (по согласованию с управляющим): ежедневно 12:00-16:00 кроме понедельника(санитарный день);  для желающих взять животное ежедневно 08:00-17:00","AdmArea":"Восточный административный округ","District":"район Вешняки",
```

Вывод с помощью **Читабельный JSON**

```json
[
    {
        "global_id": 1699129,
        "DepartmentalAffiliation": "Департамент жилищно-коммунального хозяйства города Москвы",
        "ID": 1,
        "ClarificationOfWorkingHours": "Посещение (по согласованию с управляющим): ежедневно 12:00-16:00 кроме понедельника(санитарный день);  для желающих взять животное ежедневно 08:00-17:00",
        "AdmArea": "Восточный административный округ",
        "District": "район Вешняки",
```

# Требования

Совестимые OC:
* Linux,
* Windows

Рекомендованная версия **Python 3.5** и выше

Файл должен быть в формате `.json`
# Как запустить

Пример запуска на Linux с Python 3.5:

```bash

$ python pprint_json.py <путь к файлу>

{
    "name": "Вася",
    "age": 25,
    "roles": {
        "isAdmin": false,
        "isEditor": true
    }
}
```

Запуск на Windows производится аналогичным образом

> Если файл не находится в одном каталоге с модулем `pprint_json` передавайте полный путь к файлу в качестве аргумента
```
#Linux
$ python pprint_json.py /home/Myhome/my_json_file.json

#Windows
> python pprint_json.py C:\Myfile\my_json_file.json

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)