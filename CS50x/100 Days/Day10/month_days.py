def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(input_year, input_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(input_year) == True:
        month_days[1] = 28
        month_index = input_month -1
        return month_days[month_index]
    elif is_leap_year(input_year) == False:
        month_index = input_month -1
        return month_days[month_index]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)