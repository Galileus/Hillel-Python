



while True:
    try:
        a = int(input('enter the number for a: '))
        b = int(input('enter the number for b: '))

    except Exception as e:
        print('please enter a number')
        continue

    try:
        if a or b > 0:
            print(a / b)
            break
        else:
            print(a / b)

    except Exception as e:
        print('don`t use 0 or string for b !!!')



