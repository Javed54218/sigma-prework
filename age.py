from datetime import date


def date_difference():
    """
    Calculates difference between inputted date and current date
    in years and days
    """
    while True:

        input_day = int(input("Please input a day of a month: "))
        input_month = int(input("Please input a month (01-12): "))
        input_year = int(input("Please input a year: "))

        try:
            input_date = date(input_year, input_month, input_day)
        except:
            print(
                "Date entered was inputted incorrectly or doesn't exist, please try again")
            continue

        if input_date > date.today():
            print("Date cannot be in the future, try again")
            continue
        else:
            timedelta = (date.today() - input_date).days
            break

    years = timedelta // 365
    days = timedelta % 365

    return years, days, input_date


year, day, inputted_date = date_difference()
print(f"{inputted_date} is {year} years and {day} days away from today")
