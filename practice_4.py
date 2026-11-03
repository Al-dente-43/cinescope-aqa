from collections import Counter

log = [
    "12:03:11 ERROR payment-gateway 402",
    "12:03:12 INFO movies 200",
    "12:03:13 ERROR payment-gateway 500",
    "12:03:14 INFO auth 200",
    "12:03:15 WARN movies 200",
    "12:03:16 ERROR auth 500",
    "12:03:17 INFO movies 200",
]

seats = [
    {"seat": 7, "status": "FREE",  "hall": "Зал 1"},
    {"seat": 3, "status": "sold",  "hall": "Зал 1"},
    {"seat": 5, "status": "free",  "hall": "Зал 1"},
    {"seat": 9, "status": "SOLD",  "hall": "Зал 2"},
]

levels_in_log_manual = {}
for i in log:
    level = i.split()[1]
    levels_in_log_manual[level] = levels_in_log_manual.get(level,0) + 1

levels_in_log_counter = Counter(line.split()[1] for line in log)
print(levels_in_log_manual)
print(levels_in_log_counter)



free_seats = [seat for seat in seats if seat["status"].upper() == "FREE"]

free_seats_sorted = sorted(free_seats,key = lambda m: m["seat"])
print(free_seats_sorted)

errors = Counter(line.split()[2] for line in log if line.split()[1].upper() == "ERROR")
worst_service = errors.most_common(1)[0][0] if errors else "нет"
print(errors)
worst = errors.most_common(1)[0][0]
      
is_all_seats_from_same_hall = all(h["hall"] == seats[0]["hall"] for h in seats)

final_string = f"Всего {len(log)}, ошибок {levels_in_log_counter["ERROR"]}, худший сервис {worst}"
print(final_string)
print(is_all_seats_from_same_hall)