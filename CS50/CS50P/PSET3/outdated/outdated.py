months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        if "/" in date:
            new_date = date.split("/")
            month = int(new_date[0])
            day = int(new_date[1])
            year = int(new_date[2])
            if 0 < day < 10:
                day = 0 + str(day)
            if 0 < month < 10:
                month = 0 + str(month)
            if 10 <= day <= 31:
                print(f"{year}-{month}-{day}")
                break
            else:
                continue
        elif "," in date:
            new_date = date.split(" ")
            month = new_date[0]
            day = new_date[1].split(",")
            new_day = int(day[0])
            year = new_date[2]
            if month.title() in months and 10 <= new_day <= 31 and 10 <= months.index(month.title()) <= 12:
                print(f"{year}-{months.index(month.title()) + 1}-{new_day}")
                break
            elif month.title() in months and 10 > new_day > 0 and 0 < months.index(month.title()) < 10:
                print(f"{year}-0{months.index(month.title()) + 1}-0{new_day}")
                break
            else:
                continue
    except :
        continue
