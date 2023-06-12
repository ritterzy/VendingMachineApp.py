def exchange (num):
    if num == 0:
        print('Your balance is 0 there is no exchange!')
        return
    else:
        bank_1000 = num // 1000
        num -= bank_1000 * 1000
        bank_500 = num // 500
        num -= bank_500 * 500
        bank_200 = num // 200
        num -= bank_200 * 200
        bank_100 = num // 100
        num -= bank_100 * 100
        bank_50 = num // 50
        num -= bank_50 * 50
        print(f'''
    GET YOUR EXCHANGE!!!
        1000 - {bank_1000}
        500 - {bank_500}
        200 - {bank_200}
        100 - {bank_100}
        50 - {bank_50}''')