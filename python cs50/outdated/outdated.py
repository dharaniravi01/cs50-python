def main():
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
        user_date = input("Date: ").replace(",", "").rstrip().lstrip()
        if '/' in user_date:
            x, y, z = user_date.split('/')
        elif ' ' in user_date:
            x, y, z = user_date.split(' ')
        else:
            continue
        try:
            day = int(y)
            year = int(z)
            if x.isdigit():
                month = int(x)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    new_date = f"{year}-{month:02}-{day:02}"
                    print(new_date)
                    break
                else:
                    continue
            elif x in months:
                month_num = months.index(x) + 1
                if 1 <= day <= 31:
                    new_date2 = f"{year}-{month_num:02}-{day:02}"
                    print(new_date2)
                    break

        except ValueError:
            continue



main()
