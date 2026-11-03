line_1 = "2026-09-17 12:03:11 ERROR payment-gateway 402 card declined"
line_2 = "2026-09-17 12:03:12 INFO movies 200 catalog served"
line_3 = "2026-09-17 12:03:13 error auth 500 token service unavailable"
line_4 = "  2026-09-17 12:03:14 WARN movies 200 slow query 1900ms  "

###1
line_1_arr = line_1.split()
line_1_lvl = line_1_arr[2]
line_1_service = line_1_arr[3]
line_1_code = line_1_arr[4]
if (type(line_1_code) is str):
    print(line_1_code)

line_2_arr = line_2.split()
line_3_arr = line_3.split()
line_4_arr = line_4.split()

###2
lines_arr = [line_1_arr,line_2_arr,line_3_arr, line_4_arr]
for i in lines_arr:
    if i[2].lower()=="error":
        print(f"есть ошибка в строке {i}")

###3
if (line_4.strip().split())[0] != "":
    print("Строка не пустая")

###4
for i in (0,2):
    print(lines_arr[i])
    if 400<=int(lines_arr[i][4])<=499:
        print(f"{lines_arr[i][3]}: вина клиента ({lines_arr[i][4]})")
    elif 500<=int(lines_arr[i][4])<=599:
        print(f"{lines_arr[i][3]}: вина сервера ({lines_arr[i][4]})")
    else:
        print("Норма")

###5
