# Прооект PRODUCTS:

## Все пользователи могут создавать и получать продукты.
Создает продукт:
  - Название.
  - Описание.
  - Стоимость.

Добавил дополнительный запрос DELETE.

## Стек:
## Технологии:
![Static Badge](https://img.shields.io/badge/Python-3.9-green)
![Static Badge](https://img.shields.io/badge/Django-green)
![Static Badge](https://img.shields.io/badge/REST_framework-red)
![Static Badge](https://img.shields.io/badge/PosgreSQL-blue)
![Static Badge](https://img.shields.io/badge/JS-yellow)
![Static Badge](https://img.shields.io/badge/HTML-orange)

## Клонировать проект:
```
 git clone https://github.com/frostan/PRODUCTS.git
 cd products
```
## Установить виртульное окружение:
```
 python3 -m venv venv
 source venv/bin/activate
```

## Установить pip/requirements.txt:
```
 pip install --upgrade pip
 pip install -r requirements.txt
```

## Создать суперпользователя/сделать миграции:
```
 python3 manage.py createsuperuser
 python3 manage.py makemigrations
 python3 manange.ru migrate
```

## Примеры запросов:

![Static Badge](https://img.shields.io/badge/GET-1fa7)
![Static Badge](https://img.shields.io/badge/POST-00BFFF)
![Static Badge](https://img.shields.io/badge/DEL-FF0000)


## Получение списка продуктов:
![Static Badge](https://img.shields.io/badge/GET-1fa7)```http://127.0.0.1:8000/api/products/ ```

### Ответ: ```200```
```
[
    {
        "id": 11,
        "name": "Шоколад",
        "description": "Темный с лесными орехами",
        "price": "150.00"
    }
]
```

## Добавление продуктов:
![Static Badge](https://img.shields.io/badge/POST-00BFFF)```http://127.0.0.1:8000/api/products/```

### Ответ: ```201```
```
{
    "id": 11,
    "name": "Шоколад",
    "description": "Темный с лесными орехами",
    "price": "150.00"
}
```

## Удаление продуктов:
![Static Badge](https://img.shields.io/badge/DEL-FF0000)```http://127.0.0.1:8000/api/products/pk/```

### Ответ:```204 ```
```
```