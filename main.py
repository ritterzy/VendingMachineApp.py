from VM_prod_list import product_list, write_prod_file, prod_amount_minus
from options import print_options, choose_option
import constants
from insert_banknote import insert_banknote, print_balance, check_banknote, banknotes_data, banknote_amount_plus, banknote_write
from show_av_products import show_av_products, available_products
from sel_product import select_product
from exchange_test import exchange
from VM_service import vm_service
#? we importing all our functions above



def start_vm():
    counter = 0     #! our balance
    data = product_list('VM_products.txt')
    data_banknote = banknotes_data('VD_banknotes.csv')
    while True:
        print_options()
        chose_option = choose_option()
        if chose_option == constants.INSERT_BANKNOTE:
            banknote = insert_banknote(check_banknote('VD_banknotes.csv'))
            counter += banknote
            print_balance(counter)
            banknote_amount_plus(data_banknote, banknote)
            banknote_write('VD_banknotes.csv', data_banknote)
        elif chose_option == constants.SHOW_AV_PRODUCTS:
            show_av_products(data)
        elif chose_option == constants.SELECT_PRODUCT:
            selected_product = select_product(available_products(data, counter), counter)
            while True:
                if selected_product == None:
                    break
                counter -= selected_product[0]
                print_balance(counter)
                prod_amount_minus(data, int(selected_product[1]))
                write_prod_file('VM_products.txt', data)
                break
        elif chose_option == constants.GET_CHANGE:
            exchange(counter)
            counter = 0
        elif chose_option == 178234:
            vm_service(data, data_banknote)
    

    
start_vm()