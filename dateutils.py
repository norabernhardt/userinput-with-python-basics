from datetime import date


def currentAge(birthday):
    today=date.today()
    yearDiff = today.year - birthday.year
    noBirthdayThisYear = (today.month, today.day) < (birthday.month, birthday.day)

    if noBirthdayThisYear:
        return yearDiff -1
    return yearDiff
