small = 2
regular = 5
big = 6

user_budget = input('whata is your budget? ')

try:
    user_budget = int(user_budget)

except:
    print('please enter a number')
    exit()

if user_budget > 0:
    if user_budget >= big:
        print('you can afford the big coffee')
        if user_budget == big:
            print('its complet')

        else:
            print('your change is', user_budget - big)
    elif user_budget == regular:
        print('you can afford the regular coffee')
        print('its complete')

    elif user_budget >= small:
        print('you can buy the small coffee')
        if user_budget == small:
            print('its complete')
        
        else:
            print('your change is', user_budget - small)