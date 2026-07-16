
def http_status(status):
    match status:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Error")

http_status(600)


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

day = 7
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Yay! Weekend")
    case _:
        print("Invalid Day")


month = 5
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("This month is April and the weekday is going")
    case 6 | 7 if month == 5:
        print("This month is May and the weekend is going")
    case _:
        print("Invalid day")
