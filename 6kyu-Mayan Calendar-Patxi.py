def convert_mayan(date):
    baktun, katun, tun, uinal, kin = [int(x) for x in date.split()]

    # Days in each month in our calendar
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Calculate total days from the Mayan date
    total_days = (baktun * 144000) + (katun * 7200) + (tun * 360) + (uinal * 20) + kin

    # Reference Mayan date for January 1, 2000
    reference_date = (13 * 144000) + (20 * 7200) + (7 * 360) + (16 * 20) + 3

    # Calculate the difference in days
    days_difference = total_days - reference_date

    # Calculate the Gregorian date
    year = 2000
    month = 1
    day = 1

    while days_difference > 0:
        days_in_current_month = days_in_month[month]

        # Adjust for leap year
        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days_in_current_month += 1

        if days_difference >= days_in_current_month:
            days_difference -= days_in_current_month
            month += 1
            if month > 12:
                month = 1
                year += 1
        else:
            day += days_difference
            days_difference = 0

    return f"{day} {month} {year}"
