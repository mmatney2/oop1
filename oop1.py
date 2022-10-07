secret_num = 20

while True:
    number = input('guess the num: ')

    try:
        number = int(number)
    except:
        print('sorry that is not the number')
        continue

    if number != secret_num:
        if number > secret_num:
            print(number, 'is greater than the secret num')

        elif number < secret_num:
            print(number, 'is less than secret numbe')

    else:
        print('you guessed it')
        break
