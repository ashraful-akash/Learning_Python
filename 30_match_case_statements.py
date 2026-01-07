#match-case statement (switch): an alternative to using many "elif" statements
#                               execute some code if a value matches a 'case'
#                               benefits: cleaner and syntax is more readable

def day_of_week(day):
    if day==1:
        return "It's Sunday"
    elif day==2:
        return "It's Monday"
    elif day==3:
        return "It's Tueday"
    elif day==4:
        return "It's Wednesday"
    elif day==5:
        return "It's Thursday"
    elif day==6:
        return "It's Friday"
    elif day==7:
        return "It's Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(3))


def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tueday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "Not a valid day"
    
print(day_of_week(9))

