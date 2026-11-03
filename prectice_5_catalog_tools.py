from collections import Counter


response = {
    "count": 3,
    "movies": [
        {"id": 34, "name": "Дюна", "price": 350, "published": True},
        {"id": 35, "name": "Опенгеймер", "price": 600, "published": True},
        {"id": 36, "name": "Аритмия", "price": 300, "published": False},
    ],
}

def published_names(response):
    return [movie["name"] for movie in response["movies"] if movie["published"]]

def count_cheaper(response, limit):
    return len([movie for movie in response["movies"] if int(movie["price"])<limit])

def verdict(code):
    if 200<=code<=299:
        return "ok"
    if 400<=code<=499:
        return "клиент"
    if 500<=code<=599:
        return "сервер"
    return "неизвестно"

def seat_label(row, seat, hall="Зал 1"):
    return f"{hall}, ряд {row}, место {seat}"