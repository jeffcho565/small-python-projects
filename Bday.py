import datetime
def dayOfBirth():
    year = int(input("What year were you born?: "))
    month = int(input("What month were you born?: "))
    day = int(input("What day were you born?: "))
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
        }
    Bday=datetime.datetime(year,month,day)
    weekday = Bday.weekday()
    print("You were born on a %s."%(days[weekday]))
dayOfBirth()