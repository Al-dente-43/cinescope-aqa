base_url = "https://api.dev-cinescope.artside-qa.ru"
movie_name = "Дюна"
price = 350
is_available = True 
discount = None
end_point = "movies"
movie_id = 42

print(type(base_url))
print(type(movie_name))
print(type(price))
print(type(is_available))
print(type(discount))
request_url = f"{base_url}/{end_point}/{movie_id}"
print(request_url)
print(request_url.startswith("https"))