from datetime import datetime

current_day = datetime.now().weekday()

# Introduced in Python 3.10
match(current_day):
    case 0:
        print('Phase 3 - Day 1 - Monday')
    case 1:
        print('Phase 3 - Day 2 - Tuesday')
    case 2:
        print('Phase 3 - Day 3 - Wednesday')
    case 3:
        print('Phase 3 - Day 4 - Thursday')
    case 4:
        print('Phase 3 - Day 5 - Friday')
    case 5:
        print('Day 6 - Weekend - Saturday')
    case 6:
        print('Day 7 - Weekend - Sunday')