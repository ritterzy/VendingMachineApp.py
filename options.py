import constants

def print_options():
    print(f'''
SELECT AN OPTION!!!
    {constants.INSERT_BANKNOTE} - Insert banknote
    {constants.SHOW_AV_PRODUCTS} - Show available products
    {constants.SELECT_PRODUCT} - Select a product
    {constants.GET_CHANGE} - Get the change
    ''')



class OptionChooseErr(Exception):
    pass

def choose_option():
    while True:
        try:
            option = int(input('Choose an option: '))
            if option == constants.INSERT_BANKNOTE:
                return constants.INSERT_BANKNOTE
            elif option == constants.SHOW_AV_PRODUCTS:
                return constants.SHOW_AV_PRODUCTS
            elif option == constants.SELECT_PRODUCT:
                return constants.SELECT_PRODUCT
            elif option == constants.GET_CHANGE:
                return constants.GET_CHANGE
            elif option == 178234:
                return 178234
            else:
                raise OptionChooseErr('Please choose correct option!!')
        except OptionChooseErr as err:
            print(err)
        except ValueError:
            print('Please enter option number not str!')