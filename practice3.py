response = {
    "count": 3,
    "movies": [
        {"id": 34, "name": "Дюна", "price": 350, "published": True,
         "rating": {"kp": 7.4, "imdb": 8.0}},
        {"id": 35, "name": "Опенгеймер", "price": 600, "published": True,
         "rating": {"kp": 8.2, "imdb": 8.4}},
        {"id": 36, "name": "Аритмия", "price": 300, "published": False,
         "rating": {"kp": 7.9}},
    ],
}
assert response["count"] == len(response["movies"]), "Количество фильмов не совпало"

print(f"Цена второго фильма: {response['movies'][1]["price"]}")
print(f"Рейтинг третьего фильма на KP: {response['movies'][2]["rating"]["kp"]}")
print(f"Рейтинг третьего фильма на IMDB: {response['movies'][2]["rating"].get("imdb")}")
print("Список всех фильмов:")
for i in response["movies"]:
    print(i["name"])
movies_sorted = sorted(response["movies"],key=lambda m: m["price"], reverse=True)
print(f"Самый дорогой фильм: {movies_sorted[0]["name"]}")