1. GET https://qa-internship.avito.com/api/1/item/:id
При отправке некорректного seller_id превышающий максимум приходит успешный ответ, со следующим телом ответа
9999999
[
    {
        "createdAt": "2024-09-11 17:16:08.133521 +0300 +0300",
        "id": "6359a483-dae8-4231-adc8-c71c5f1eb401",
        "name": "Телефон",
        "price": 999,
        "sellerId": 9999999,
        "statistics": {
            "contacts": 15,
            "likes": 0,
            "viewCount": 2
        }
    }
]

2. POST https://qa-internship.avito.com/api/1/item  body{}
При создании объявления в случае отправки пустого тела ответ 500
{"message":"internal error","code":500}
 
3. POST https://qa-internship.avito.com/api/1/item c body {
        "name": "",
        "price": 85566,
        "sellerId": 345222,
        "statistics": {
            "contacts": 7,
            "like": 7,
            "viewCount": 1
        }
    }
При отправке сообщения без имени запись сохраняется

4. GET https://qa-internship.avito.com/api/1/item/:id
При отправке некорректного seller_id возвращается статус код 200