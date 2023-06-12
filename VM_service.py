import constants
from insert_banknote import banknote_write
from VM_prod_list import write_prod_file


def vm_service(data, bank_data):
    while True:
        print_service_options()
        chose_option = choose_option()
        if chose_option == constants.SET_ALL_PRODUCTS_TO_MAX:
            set_all_prods_to_max(data)
            write_prod_file('VM_products.txt', data)
        elif chose_option == constants.SET_COINS_TO_MAX:
            coins_to_max()
        elif chose_option == constants.GET_ALL_CASH:
            get_all_cash(bank_data)
            banknote_write('VD_banknotes.csv', bank_data)
        elif chose_option == constants.BACK_TO_MAIN_MENU:
            return




def print_service_options():
    print('''
    Options:
    1 - Set the remaining quantity of all products to maximum
    2 - Set the remaining amount of each coin denomination to maximum
    3 - Get all cash(Reset banknote's amounts to 0)
    4 - Back to main menu
    ''')
 
 


class OptionChooseErr(Exception):
    pass
def choose_option():
    while True:
        try:
            option = int(input('Choose an option: '))
            if option == constants.SET_ALL_PRODUCTS_TO_MAX:
                return constants.SET_ALL_PRODUCTS_TO_MAX
            elif option == constants.SET_COINS_TO_MAX:
                return constants.SET_COINS_TO_MAX
            elif option == constants.GET_ALL_CASH:
                return constants.GET_ALL_CASH
            elif option == constants.BACK_TO_MAIN_MENU:
                return constants.BACK_TO_MAIN_MENU
            else:
                raise OptionChooseErr('Please choose correct option!!')
        except OptionChooseErr as err:
            print(err)
        except ValueError:
            print('Please enter option number not str!')



def set_all_prods_to_max(data):
    for product in data:
        product['amount'] = 15
    print('Operation was succesfully!')
    return


def coins_to_max():
    print("This function doesn't work yet, coming soon!")
    return


def get_all_cash(data):
    sum = 0
    i = 0
    for banknote in data:
        if i == 0:
            i += 1
            continue
        else:
            print(f'{banknote[0]} - {banknote[1]}')
            sum = sum + banknote[0] * banknote[1]
            banknote[1] = 0
    print(f'Summ is {sum}, get all cash!')
    return data
        
